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
    if len(lst_obj) > 0:
        min_el = lst_obj[0]
        for ind in range(1, len(lst_obj)):
            if min_el > lst_obj[ind]:
                min_el = lst_obj[ind]
        return min_el
    else:
        return None


# O(n^2)
def find_min_v2(lst_obj: list):
    def is_min(list_obj: list, el: int):
        result = True
        for ind in range(1, len(list_obj)):
            if el > list_obj[ind]:
                result = False

        return result

    for ind in range(1, len(lst_obj)):
        if is_min(lst_obj, lst_obj[ind]):
            return lst_obj[ind]


arr = list([random.randrange(1, 30) for el in range(1, 16)])

print(arr)
print(find_min(arr))
print(find_min_v2(arr))
