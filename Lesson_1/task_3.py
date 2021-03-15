"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""


# O(n^2)
def find_max(list_obj: list, count: int):
    def find_max_ind(list_obj: list):  # O(n)
        res_ind = 0  # O(1)
        for ind in range(len(list_obj)):  # O(n)
            if list_obj[res_ind][1] < list_obj[ind][1]:  # O(1)
                res_ind = ind  # O(1)
        return res_ind  # O(1)
    res = []  # O(1)
    buf = list_obj.copy()  # O(n)
    for i in range(count):  # O(n)
        tmp_ind = find_max_ind(buf)  # O(n)
        res.append(buf[tmp_ind])  # O(1)
        buf.pop(tmp_ind)  # O(n)
    return res  # O(1)


# O(n* log n)
def find_max_v2(list_obj: list, count: int):
    buf = list_obj.copy()  # O(n)
    buf = sorted(buf, key=lambda t: t[1], reverse=True) # O(n*log n)
    return buf[:count]  # O(n)


lst = [
    ('Microsoft', 1500000),
    ('Oracle', 1000000),
    ('HP', 7500000),
    ('Dell', 10000)
]

print(lst)
print(find_max(lst, 3))
print(find_max_v2(lst, 3))

# find_max_v2 эффективнее, т.к. имеет сложность O(n*log n) против O(n^2) у find_max
