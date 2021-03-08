"""
    Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

number = int(input("Введите трехзначное число: "))
if 100 <= number <= 999:
    units = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    sum_digits = units + tens + hundreds
    mul_digits = units * tens * hundreds
    print(f'Сумма цифр числа {number} = {sum_digits}.')
    print(f'Произведение цифр числа {number} = {mul_digits}.')
else:
    print('Введенное число не трехзначное')
