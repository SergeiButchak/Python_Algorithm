"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


lst = [i for i in range(10)]
lst2 = [i for i in range(1000)]
lst3 = [i for i in range(100000)]
print(timeit('func_1(lst)', globals=globals(), number=100000))
print(timeit('func_2(lst)', globals=globals(), number=100000))
print(timeit('func_1(lst2)', globals=globals(), number=1000))
print(timeit('func_2(lst2)', globals=globals(), number=1000))
print(timeit('func_1(lst3)', globals=globals(), number=10))
print(timeit('func_2(lst3)', globals=globals(), number=10))
"""
Код достаточно простой, по сути оптимизировать зесь нечего. Можно заменить обычный цикл списоковым включением, 
но замеры показывают, что прирост скорости при этом мизерный.

0.1927894
0.19692149999999997
0.16000569999999997
0.12135370000000001
0.17066249999999994
0.15255509999999994

"""