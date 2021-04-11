"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""
from random import randint


class BinaryTree:
    def __init__(self, root_obj=None):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    def add_elem(self, data):
        if self.root is None:
            self.root = data
        elif data < self.root:
            if self.left_child is None:
                self.left_child = BinaryTree(data)
            else:
                self.left_child.add_elem(data)
        else:
            if self.right_child is None:
                self.right_child = BinaryTree(data)
            else:
                self.right_child.add_elem(data)

    def symmetric_walk(self):
        if self.root is None:
            return
        if self.left_child is not None:
            self.left_child.symmetric_walk()
        print(self.root)
        if self.right_child is not None:
            self.right_child.symmetric_walk()


arr = [randint(1, 1000) for i in range(15)]
r = BinaryTree()
for el in arr:
    r.add_elem(el)
print(arr)
r.symmetric_walk()

"""
Добавлен метод добавления эелемента в дерево add_elem, по принципу если новый елемент меньше листа, элемент сохраняется 
в левой ветви, если больше то в правой. Если у ветвей уже есть листья, новые элемент передается на уровень ниже.
Добавлен метод симметричного обхода дерева symmetric_walk
"""