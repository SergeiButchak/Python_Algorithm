"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

# hash?


def uniq_substr(string: str):
    substr_set = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            buf = string[i:j+1]
            substr_set.add(hash(buf))
    return substr_set


input_str = 'papa'
str_set = uniq_substr(input_str)
print(f"{input_str} - {len(str_set)} уникальных подстрок.")

