"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
# sqlite, postgres, db_api, orm

from hashlib import sha256


def get_hash(password: str, salt: str):
    return sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()


def save_pass(str_hash: str, file_name: str):
    with open(file_name, 'a') as file_out:
        file_out.write(str_hash)
        file_out.write('\n')


def check_password(password: str, salt: str, file_name: str):
    res = False
    str_hash = get_hash(password, salt)
    with open(file_name) as file_in:
        for line in file_in:
            if line.strip() == str_hash:
                res = True
                break
    return res


file_nm = "pass.txt"
str_salt = "SecretKey"

# for i in range(0, 5):
#     str_pass = input("Введите пароль: ")
#     save_pass(get_hash(str_pass, str_salt), file_nm)

str_pass = input("Введите пароль: ")
chk_res = check_password(str_pass, str_salt, file_nm)
if chk_res:
    print("Пароль верен.")
else:
    print("Пароль неправильный.")