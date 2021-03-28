"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
from timeit import timeit
from random import randint

array = [randint(1, 9) for i in range(100)] # [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    max_count = [0, 0]
    elem_counter = dict()
    for el in array:
        if elem_counter.get(el) is None:
            elem_counter[el] = 1
        else:
            elem_counter[el] = elem_counter[el] + 1
        if elem_counter[el] > max_count[1]:
            max_count[0] = el
            max_count[1] = elem_counter[el] + 1
    return f'Чаще всего встречается число {max_count[0]}, ' \
           f'оно появилось в массиве {max_count[1]} раз(а)'


print(timeit("func_1()", globals=globals(), number=10000))
print(timeit("func_2()", globals=globals(), number=10000))
print(timeit("func_3()", globals=globals(), number=10000))

"""
У первых двух вариантов сложность O(n^2). Плюс во второй функции мы все подсчитанные эелементы сохраняем в отдельный 
массив, затем происходит поиск максимального значения и поиск его индекса в новом массиве, что дает дополнительно O(2n). 
В итоге вторая функция будет работать медленнее первой. Это подтверждается замерами. Для оптимизации можно использовать
словарь для хранения значений элементов и их количества, что позволит перебрать все элементы и подсчитать их частоту за
один проход по массиву, в итоге получив сложность O(n). Что наглядно подтверждается замерами при увеличении размера
воходного массива.

Размер массива 100 элементов:
2.1729797
2.2524765
0.35207540000000037

"""