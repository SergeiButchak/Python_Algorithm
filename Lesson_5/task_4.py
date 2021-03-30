"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit


def fill_dict(obj: dict, count: int):
    for i in range(count):
        obj[i] = i


def fill_o_dict(obj: OrderedDict, count: int):
    for i in range(count):
        obj[i] = i


dct = dict()
odct = OrderedDict()

print('Заполнение dict: ', timeit("fill_dict(dct, 100)", number=100000, globals=globals()))
print('Заполнение OrderDict: ', timeit("fill_o_dict(dct, 100)", number=100000, globals=globals()))
fill_dict(dct, 100001)
fill_o_dict(odct, 100001)
print('Метод get в dict: ', timeit("dct.get(5)", number=100000, globals=globals()))
print('Метод get в OrderDict: ', timeit("odct.get(5)", number=100000, globals=globals()))
print('Метод items в dict: ', timeit("dct.items()", number=100000, globals=globals()))
print('Метод items в OrderDict: ', timeit("odct.items()", number=100000, globals=globals()))
print('Метод setdefault в dict: ', timeit("dct.setdefault(5, 0)", number=100000, globals=globals()))
print('Метод setdefault в OrderDict: ', timeit("odct.setdefault(5, 0)", number=100000, globals=globals()))
print('Метод values в dict: ', timeit("dct.values()", number=100000, globals=globals()))
print('Метод values в OrderDict: ', timeit("odct.values()", number=100000, globals=globals()))
print('Метод popitem в dict: ', timeit("dct.popitem()", number=100000, globals=globals()))
print('Метод popitem в OrderDict: ', timeit("odct.popitem()", number=100000, globals=globals()))

"""
По замерам особой разницы между dict и OrderDict нет. Особенность OrderDict заключается в том, что он 'умеет' запоминать
порядок, в котором элементы добавлялись в словарь, соответственно OrderDict имеет смысл применять в задачах, 
где эта особенность имеет значение
Заполнение dict:  0.6393441
Заполнение OrderDict:  0.5706215
Метод get в dict:  0.009989899999999885
Метод get в OrderDict:  0.010815200000000136
Метод items в dict:  0.011224600000000029
Метод items в OrderDict:  0.011096800000000018
Метод setdefault в dict:  0.011953799999999903
Метод setdefault в OrderDict:  0.013576100000000091
Метод values в dict:  0.010471300000000072
Метод values в OrderDict:  0.010961999999999916
Метод popitem в dict:  0.015234600000000098
Метод popitem в OrderDict:  0.02695000000000003
"""