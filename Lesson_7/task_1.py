"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
from timeit import timeit


def bubble_sort_v1(array: list):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def bubble_sort_v2(array: list):
    for i in range(len(array)):
        is_change = False
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_change = True
        if not is_change:
            break


def bubble_sort_v3(array: list):
    last_index = len(array) - 1
    for i in range(len(array)):
        for j in range(last_index):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                last_index = j


arr_1 = [randint(-100, 100) for i in range(50)]
arr_2 = arr_1.copy()
arr_3 = arr_1.copy()
print(timeit("bubble_sort_v1(arr_1.copy())", globals=globals(), number=10000))
print(timeit("bubble_sort_v2(arr_1.copy())", globals=globals(), number=10000))
print(timeit("bubble_sort_v3(arr_1.copy())", globals=globals(), number=10000))
print(arr_1)
bubble_sort_v1(arr_1)
print(arr_1)
bubble_sort_v2(arr_2)
print(arr_2)
bubble_sort_v3(arr_3)
print(arr_3)
"""
Первоначальная идея: если за проход по списку не совершается ни одной сортировки, то завершение. При этом в некоторых 
случаях для частично упорядоченного массива позволяет сократить число проходов по массиву. На пракитке при случайном 
наборе данных прирост производительности незначительный либо отсутствует совсем.

Вторая идея: запоминать индекс последнего переставленного элемента, делая предположение о том, что если после элемента i
не было перестановок, то элементы начиная с  i-ого до конца массива являются уже упорядочеными. Это позоволяет в случае
частично упорядоченного массива сокращать количество сравнений при очередном проходе. Замеры на практике показывают, что
для определенных случаев можно получить небольшое увелиечение производительности.

3.2212476
3.1538159
2.8858505999999995
[-67, -4, 13, 44, 58, 99, -29, 65, -70, -18, -83, -10, 45, 62, 41, 34, -41, -20, -73, -79, 100, 65, 92, -81, -28, -76, 
22, -37, -99, -72, -77, -5, 64, -97, -55, 69, 10, 97, 42, 87, 59, -78, 2, 5, 44, -35, 37, -75, 32, -39]
[100, 99, 97, 92, 87, 69, 65, 65, 64, 62, 59, 58, 45, 44, 44, 42, 41, 37, 34, 32, 22, 13, 10, 5, 2, -4, -5, -10, -18, 
-20, -28, -29, -35, -37, -39, -41, -55, -67, -70, -72, -73, -75, -76, -77, -78, -79, -81, -83, -97, -99]
[100, 99, 97, 92, 87, 69, 65, 65, 64, 62, 59, 58, 45, 44, 44, 42, 41, 37, 34, 32, 22, 13, 10, 5, 2, -4, -5, -10, -18, 
-20, -28, -29, -35, -37, -39, -41, -55, -67, -70, -72, -73, -75, -76, -77, -78, -79, -81, -83, -97, -99]
[100, 99, 97, 92, 87, 69, 65, 65, 64, 62, 59, 58, 45, 44, 44, 42, 41, 37, 34, 32, 22, 13, 10, 5, 2, -4, -5, -10, -18, 
-20, -28, -29, -35, -37, -39, -41, -55, -67, -70, -72, -73, -75, -76, -77, -78, -79, -81, -83, -97, -99]
"""
