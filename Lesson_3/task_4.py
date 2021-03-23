"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from hashlib import sha256


def get_hash(string: str, salt: str):
    return sha256(string.encode('utf-8') + salt.encode('utf-8')).hexdigest()


def check_url(url_str: str, salt: str, cash_url: set):
    buf = set()
    buf.add(get_hash(url_str, salt))
    return cash_url.isdisjoint(buf) ^ True


cash = set()
str_salt = "http"
cash.add(get_hash("yandex.ru", str_salt))
cash.add(get_hash("google.ru", str_salt))
cash.add(get_hash("mail.ru", str_salt))
cash.add(get_hash("rambler.ru", str_salt))

print(check_url("ya.ru", "http", cash))
print(check_url("yandex.ru", "http", cash))
