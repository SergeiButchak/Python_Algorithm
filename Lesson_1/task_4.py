"""
Задание 4.

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
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""


# O(n)
def auth(base: dict, login: str, pswd: str):
    for el in base:  # O(n)
        if login == el:  # O(1)
            if not base[el][1]:  # O(1)
                print("Требуестя активация учетной записи.")  # O(1)
                return False  # O(1)
            elif base[el][0] == pswd:  # O(1)
                print("Авторизация пройдена")  # O(1)
                return True  # O(1)
            else:  # O(1)
                print("Неверный пароль")  # O(1)
                return False  # O(1)

    print("Пользователь не найден")  # O(1)
    return False  # O(1)


# O(1)
def auth_v2(base: dict, login: str, pswd: str):
    user = base.get(login)  # O(1)
    if user is None:  # O(1)
        print("Пользователь не найден")  # O(1)
        return False  # O(1)
    if not user[1]:  # O(1)
        print("Требуестя активация учетной записи.")  # O(1)
        return False  # O(1)
    elif user[0] == pswd:  # O(1)
        print("Авторизация пройдена")  # O(1)
        return True  # O(1)
    else:  # O(1)
        print("Неверный пароль")  # O(1)
        return False  # O(1)


users = {
    "user1": ("dghlsdghal", True),
    "user2": ("dghlsdghal", True),
    "user3": ("dghlsdghal", False),
    "user4": ("dghlsdghal", True),
    "user5": ("dghlsdghal", True),
}

print(auth(users, "user1", "dghlsdgha"))
print(auth(users, "user2", "dghlsdghal"))
print(auth(users, "user3", "dghlsdghal"))
print(auth(users, "user33", "dghlsdghal"))
print(auth_v2(users, "user1", "dghlsdgha"))
print(auth_v2(users, "user2", "dghlsdghal"))
print(auth_v2(users, "user3", "dghlsdghal"))
print(auth_v2(users, "user33", "dghlsdghal"))

# auth_v2 эффективнее, т.к. имеет сложность O(1) против O(n) у auth
