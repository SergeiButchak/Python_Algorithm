"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснвование рез-ам
"""
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def simple_2(num: int):
    n = 3
    simple_nums = [2]
    while len(simple_nums) < num:
        is_simple = True
        for el in simple_nums:
            if n % el == 0:
                is_simple = False
                break
        if is_simple:
            simple_nums.append(n)
        n += 1
    return simple_nums[num - 1]


# i = int(input('Введите порядковый номер искомого простого числа: '))
print("simple(10)")
print(timeit("simple(10)", globals=globals(), number=100))
print("simple_2(10)")
print(timeit("simple_2(10)", globals=globals(), number=100))
print("simple(100)")
print(timeit("simple(100)", globals=globals(), number=10))
print("simple_2(100)")
print(timeit("simple_2(100)", globals=globals(), number=10))
print("simple(1000)")
print(timeit("simple(1000)", globals=globals(), number=1))
print("simple_2(1000)")
print(timeit("simple_2(1000)", globals=globals(), number=1))

"""
Считается что сложность у наивного перебора O(n^(1/2)), у решета Эратосфена сложность O(n*log(log n)). 
Замеры показывают, что даже при небольших n, решето Эрфтосфена эффективнее простого перебора.

simple(10)
0.0024322999999999984
simple_2(10)
0.0009399000000000074
simple(100)
0.02434080000000001
simple_2(100)
0.0030102000000000045
simple(1000)
0.4047107
simple_2(1000)
0.03707729999999998
"""