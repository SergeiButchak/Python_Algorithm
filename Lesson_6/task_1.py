"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from timeit import default_timer
from memory_profiler import memory_usage
from pympler import asizeof


def profiler(func):
    def wrapper(*args):
        start_time = default_timer()
        start_mem = memory_usage()
        func(*args)
        end_time = default_timer()
        end_mem = memory_usage()
        print(f"Время выполнения: {end_time - start_time}\nИспользование памяти: {end_mem[0] - start_mem[0]}")

    return wrapper


# 1


@profiler
def revers_1(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


@profiler
def revers_2(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print("Пример 1.")
revers_1(123456789723857203975832175327594375983475094375293475024582340967140721343282138509475)
revers_2(123456789723857203975832175327594375983475094375293475024582340967140721343282138509475)

"""
Пример 1.
Время выполнения: 0.11078390000000005
Использование памяти: 0.0078125
Время выполнения: 0.10835779999999995
Использование памяти: 0.0

Вторая функция оптимизирована при помощи встроенной функции str и требует меньше памяти и меньше времени
"""
# 2


@profiler
def create_list(size):
    return [i for i in range(size)]


@profiler
def generate_list(size):
    for i in range(size):
        yield i


print("Пример 2.")
create_list(1000000)
generate_list(1000000)

'''
Пример 2.
Время выполнения: 0.25130450000000004
Использование памяти: 0.23828125
Время выполнения: 0.11193340000000007
Использование памяти: 0.0
Тесты показывают, что использование генераторов экономичнее по использованию памяти и времени выполнения, чем списки
'''

# 3


class Car:
    def __init__(self, color, name, speed):
        self.color = color
        self.name = name
        self.speed = speed
        is_police = False

    def go(self):
        print("Машина поехала")

    def stop(self):
        self.speed = 0
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на {direction}")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}")


class CarWithSlots:
    __slots__ = ['color', 'name', 'speed', 'is_police']

    def __init__(self, color, name, speed):
        self.color = color
        self.name = name
        self.speed = speed
        is_police = False

    def go(self):
        print("Машина поехала")

    def stop(self):
        self.speed = 0
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на {direction}")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}")


obj_1 = Car("Red", "Toyota", 3500)
obj_2 = CarWithSlots("Red", "Toyota", 3500)
print("Пример 3")
print(f"Размер обычного объекта {asizeof.asizeof(obj_1)}")
print(f"Размер объекта со слотами {asizeof.asizeof(obj_2)}")

"""
Размер обычного объекта 464
Размер объекта слотами 208
Использование __slots__ позволяет сократить ресурсы на хранение атрибутов класса.
"""
