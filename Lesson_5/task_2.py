"""
2.*	Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
"""

from collections import deque


def deque_to_str(dq: deque):
    res = ''
    for i in dq:
        res += i
    return res


def add_hex(num_1: deque, num_2: deque):
    res = int(deque_to_str(num_1), 16) + int(deque_to_str(num_2), 16)
    res = f"{res:X}"
    return deque(res)


def mul_hex(num_1: deque, num_2: deque):
    res = int(deque_to_str(num_1), 16) * int(deque_to_str(num_2), 16)
    res = f"{res:X}"
    return deque(res)


first_num = deque(input('Введите первое число: '))
second_num = deque(input('Введите второе число: '))

print(list(add_hex(first_num, second_num)))
print(list(mul_hex(first_num, second_num)))
