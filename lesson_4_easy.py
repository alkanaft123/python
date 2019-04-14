# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random

lst = [random.randint(0, 9) for _ in range(10)]
print(lst)
lst = [el * el for el in lst]
print(lst)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

lst = ['apple', 'orange', 'banana']
lst_2 = ['grape', 'orange', 'banana']
print([el for el in lst if lst_2.count(el) > 0])


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

def correct(el: int):
    if el % 3 == 0 and el > 0 and not el % 4 == 0:
        return True
    else:
        return False


lst = [random.randint(-9, 9) for _ in range(10)]
print(lst)
print([el for el in lst if correct(el)])
