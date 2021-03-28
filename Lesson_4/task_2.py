"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Если у вас есть идеи, предложите вариант оптимизации, если мемоизация не имеет смысла.
Без аналитики задание считается не принятым
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))


def reverse(num: int):
    return str(num)[::-1]


print('Оптимизированная функция reverse')
print(
    timeit(
        'reverse(num_100)',
        setup='from __main__ import reverse, num_100',
        number=10000))
print(
    timeit(
        'reverse(num_1000)',
        setup='from __main__ import reverse, num_1000',
        number=10000))
print(
    timeit(
        'reverse(num_10000)',
        setup='from __main__ import reverse, num_10000',
        number=10000))

"""
Мемоизация применима там, где во входных данных часто встречаются повторяющиеся элементы. За счет сохранения результатов
мемоизация исключает повторные вычисления для одних и тех же данных. В данном случае мемоизация дает хороший прирост 
скорости, за счет того, что для замеров используются константые значения. Но в реальной ситуации, на како-нибудь большом
наборе входных данных эффект от мемоизаци может сильно меняться в зависимости от наличия повторяющихся элементов. Здесь 
же можно упростить код заменив рекурсию встроенными функциями.

Не оптимизированная функция recursive_reverse
0.029410500000000006
0.035496
0.0681349
Оптимизированная функция recursive_reverse_mem
0.002608300000000008
0.002973200000000009
0.002629500000000007
Оптимизированная функция reverse
0.004801300000000008
0.0044621999999999995
0.005986600000000009
"""