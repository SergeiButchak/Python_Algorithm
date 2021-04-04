"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile
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


@profile()
def wrapper(func, arg):
    return func(arg)


arr = [randint(-1000, 1000) for i in range(1000)]
wrapper(merge_sort, arr)
'''
Для правильного профилирования рекурсивных функций требуется создать функцию-обертку.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    40     19.6 MiB     19.6 MiB           1   @profile()
    41                                         def wrapper(func, arg):
    42     19.6 MiB      0.0 MiB           1       return func(arg)
'''
