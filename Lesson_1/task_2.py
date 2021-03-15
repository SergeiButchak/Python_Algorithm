"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""
import random


# O(n)
def find_min(lst_obj: list):
    if len(lst_obj) > 0:  # O(1)
        min_el = lst_obj[0]  # O(1)
        for ind in range(1, len(lst_obj)):  # O(n)
            if min_el > lst_obj[ind]:  # O(1)
                min_el = lst_obj[ind]  # O(1)
        return min_el  # O(1)
    else:
        return None  # O(1)


# O(n^2)
def find_min_v2(lst_obj: list):
    def is_min(list_obj: list, el: int):  # O(n)
        result = True  # O(1)
        for ind in range(1, len(list_obj)):  # O(n)
            if el > list_obj[ind]:  # O(1)
                result = False  # O(1)

        return result  # O(1)

    for ind in range(1, len(lst_obj)):  # O(n)
        if is_min(lst_obj, lst_obj[ind]):  # O(n)
            return lst_obj[ind]  # O(1)


arr = list([random.randrange(1, 30) for el in range(1, 16)])

print(arr)
print(find_min(arr))
print(find_min_v2(arr))

# find_min эффективнее, т.к. имеет сложность O(n) против O(n^2) у find_min_v2
