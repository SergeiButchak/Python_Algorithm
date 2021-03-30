"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""

from timeit import timeit
from collections import deque

ls = list()
dq = deque()

print('ls.append(1) ', timeit('ls.append(1)', globals=globals()))
print('dq.append(1)  ',timeit('dq.append(1)', globals=globals()))
ls.clear()
dq.clear()
print('ls.insert(0, 1) ', timeit('ls.insert(0, 1)', number=100000, globals=globals()))
print('dq.appendleft(1) ', timeit('dq.appendleft(1)', number=100000, globals=globals()))
ls.clear()
dq.clear()
print('ls.insert(len(ls) // 2, 1) ', timeit('ls.insert(len(ls) // 2, 1)', number=100000, globals=globals()))
print('dq.insert(len(dq) // 2, 1) ', timeit('dq.insert(len(dq) // 2, 1)', number=100000, globals=globals()))
print('ls.count(1) ', timeit('ls.count(1)', number=100000, globals=globals()))
print('dq.count(1) ', timeit('dq.count(1)', number=100000, globals=globals()))
print('ls.copy() ', timeit('ls.copy()', number=100000, globals=globals()))
print('dq.copy() ', timeit('dq.copy()', number=100000, globals=globals()))
print('ls[0] ', timeit('ls[0]', globals=globals()))
print('dq[0] ', timeit('dq[0]', globals=globals()))
print('ls[len(ls) // 2] ', timeit('ls[len(ls) // 2]', globals=globals()))
print('dq[len(ls) // 2] ', timeit('dq[len(ls) // 2]', globals=globals()))
print('ls[len(ls) - 1] ', timeit('ls[len(ls) - 1]', globals=globals()))
print('dq[len(ls) - 1] ', timeit('dq[len(ls) - 1]', globals=globals()))

"""
Вставка в конец чуть быстрее для дека
ls.append(1)  0.12642159999999997
dq.append(1)   0.07292219999999996

Вставка в начало значительно быстрее у дека
ls.insert(0, 1)  4.8671833
dq.appendleft(1)  0.009862000000000037

Вставка в середину проходит быстрей уже для списка
ls.insert(len(ls) // 2, 1)  2.9500848999999993
dq.insert(len(dq) // 2, 1)  8.980603600000002

Поиск и подсчет элементов происходит быстрее в списке
ls.count(1)  22.240550600000002
dq.count(1)  76.7931853

Список копируется быстрее дека
ls.copy()  63.373548
dq.copy()  195.99596509999998

Доступ к крайним элементам приблизительно одинаков для обоих объектов, при доступе к средним элемента дек проигрывает 
списку
ls[0]  0.06362259999997377
dq[0]  0.07225379999999859
ls[len(ls) // 2]  0.24735719999995354
dq[len(ls) // 2]  7.533227899999986
ls[len(ls) - 1]  0.1645331000000283
dq[len(ls) - 1]  0.1530872999999815

По итогу можно сделать вывод, что дек быстро работает с крайними элементами и хорошо подходит для организации таких
структур данных как стек и очередь, когда же требуется обрабатывать все элементы, то больше подойдет список.
"""