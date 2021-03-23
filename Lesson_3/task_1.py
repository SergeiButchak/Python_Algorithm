"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""

from time import time


def time_measure(function):
    def wrapper(*args):
        start = time()
        ret = function(*args)
        end = time()
        print(f"{function.__name__} - {end - start}")
        return ret
    return wrapper


@time_measure
def fill_list(_lst: list):
    for e in range(0, 10000000):
        _lst.append(e)


@time_measure
def fill_dict(_dct: dict):
    for e in range(0, 10000000):
        _dct[e] = e


@time_measure
def for_list(_lst: list):
    for el in _lst:
        pass


@time_measure
def for_dict(_dct: dict):
    for el in _dct:
        pass


@time_measure
def clear_list(_lst: list):
    _lst.clear()


@time_measure
def clear_dict(_dct: dict):
    _dct.clear()


lst = list()
dct = dict()
fill_list(lst)
fill_dict(dct)
# по времени заполнения список мало отличается от словаря
for_list(lst)
for_dict(dct)
# перебор елементов в списке происходит быстрее, т.к. список сожержит меньше данных - только значенияя своих элементов
clear_list(lst)
clear_dict(dct)
# удаление елементов в списке происходит быстрее, т.к. список сожержит меньше данных - только значенияя своих элементов
