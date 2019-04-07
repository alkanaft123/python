# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]


import math

lst_1 = [2, -5, 8, 9, -25, 25, 4]
lst_2 = []
for el in lst_1:
    if el > 0:
        sqr = math.sqrt(el)
        if sqr%1 == 0:
            lst_2.append(sqr)
print(lst_2)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = '02.11.2013'
days = ["one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one",
        "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven",
        "twenty eight", "twenty nine", "thirty", "thirty one"]
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
d = int(date[0:2])
m = int(date[3:5])
y = int(date[6:10])
print('{} {} {} year'.format(days[d - 1],month[m - 1], y))


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
n = ''
while n.isdigit() == False:
    n = input('Please enter n')
n = int(n)
lst = []
for i in range(n):
    lst.append(random.randint(-100,100))
print(lst)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]


lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst_2 = []
el_2 = ''
for el in sorted(lst):
    if el_2 != el:
        lst_2.append(el)
    el_2 = el
print(lst_2)


lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst_2 = []
for el in lst:
    if lst.count(el) == 1:
        lst_2.append(el)
print(lst_2)
