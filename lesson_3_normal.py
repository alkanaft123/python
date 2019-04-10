# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    el_1 = 1
    el_2 = 1
    if n < 2:
        print(el_1)
    for counter in range(3, m + 2):
        el_1, el_2 = el_2, el_1
        el_2 = el_2 + el_1
        if counter > n:
            print(el_1)


fibonacci(10, 30)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for o in range(1, len(origin_list)):
        if origin_list[o - 1] > origin_list[o]:
            for c in range(0, o):
                if origin_list[c] > origin_list[o]:
                    origin_list.insert(c, origin_list.pop(o))
    print(origin_list)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def fltr(f, arg: list):
    new_list = []
    for x in arg:
        if f(x):
            new_list.append(x)
    return new_list


print(fltr(lambda x: x > 0, [111, 2, -1, 3, 0.5, -10]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parar(a: list, b: list, c: list, d: list) -> bool:
    if (a[0] - b[0]) * (c[1] - d[1]) == (a[1] - b[1]) * (c[0] - d[0]):
        return True
    else:
        return False


a = [-9, -3]
b = [-5, 2]
c = [7, 3]
d = [3, -2]
print(parar(a, c, b, d))
