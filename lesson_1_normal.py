__author__ = 'Григорьев Федор Александрович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

x = 58375
x = str(x)
counter = 0
max = 0
while counter < len(x):
    if int(x[counter]) > max:
        max = int(x[counter])
    counter+=1
print(max)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = input("Please enter first value")
b = input("Please enter second value")
a,b=b,a
print(a)
print(b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

a = "asd"
while a.isdigit() == False:
    a = input("Please enter first coefficient")
a = int(a)

b = "asd"
while b.isdigit() == False:
    b = input("Please enter second coefficient")
b = int(b)

c = "asd"
while c.isdigit() == False:
    c = input("Please enter third coefficient")
c = int(c)

dis = b*b - 4*a*c
if dis < 0:
    print("The equation hasn't roots")
else:
    x1 = (-b + math.sqrt(dis)) / (2 * a)
    x2 = (-b - math.sqrt(dis)) / (2 * a)
    print(x1)
    print(x2)
