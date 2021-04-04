"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from timeit import timeit
from random import randint


def merge_sort(array: list):
    if len(array) == 1 or len(array) == 0:
        return
    left, right = array[:len(array) // 2], array[len(array) // 2:]
    merge_sort(left)
    merge_sort(right)
    left_ind = right_ind = buf_ind = 0
    buf = [0] * (len(left) + len(right))
    while left_ind < len(left) and right_ind < len(right):
        if left[left_ind] <= right[right_ind]:
            buf[buf_ind] = left[left_ind]
            left_ind += 1
        else:
            buf[buf_ind] = right[right_ind]
            right_ind += 1
        buf_ind += 1
    while left_ind < len(left):
        buf[buf_ind] = left[left_ind]
        left_ind += 1
        buf_ind += 1
    while right_ind < len(right):
        buf[buf_ind] = right[right_ind]
        right_ind += 1
        buf_ind += 1
    for i in range(len(array)):
        array[i] = buf[i]


num = int(input("Введите число элементов: "))
arr = [randint(0, 5000) / 100 for i in range(num)]
print(f"Исходный - {arr}")
merge_sort(arr)
print(f"Отсортированный - {arr}")
arr_1 = [randint(0, 5000) / 100 for i in range(10)]
arr_2 = [randint(0, 5000) / 100 for i in range(100)]
arr_3 = [randint(0, 5000) / 100 for i in range(1000)]
print("array 10 ", timeit("merge_sort(arr_1.copy())", globals=globals(), number=10000))
print("array 100 ", timeit("merge_sort(arr_2.copy())", globals=globals(), number=10000))
print("array 1000 ", timeit("merge_sort(arr_3.copy())", globals=globals(), number=10000))

"""
Введите число элементов: 10
Исходный - [25.18, 23.43, 29.64, 25.26, 44.74, 2.69, 37.95, 12.93, 43.51, 5.53]
Отсортированный - [2.69, 5.53, 12.93, 23.43, 25.18, 25.26, 29.64, 37.95, 43.51, 44.74]
array 10  0.2530400000000004
array 100  5.4767491999999995
array 1000  81.7287784
"""
