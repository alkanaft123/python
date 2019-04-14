import re
import random

# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]

# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

print(*list(map(list, zip(*matrix))), sep='\n')

# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

pattern = '(?=(\d\d\d\d\d))'
lst = re.findall(pattern, number)
max = 0
counter_max = None

for idx, el in enumerate(lst):
    product = 1
    for i in el:
        product *= int(i)
    if product > max:
        max = product
        counter_max = idx
print('Max =', max, ' counter =', counter_max, ' number =', lst[counter_max])


# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

def print_matrix(queens):
    desk = [[' - ' for _ in range(8)] for _ in range(8)]
    for el in queens:
        desk[el[0]][el[1]] = ' * '
    for i in range(len(desk)):
        for j in range(len(desk[i])):
            print("{}".format(desk[i][j]), end="")
        print()


def make_desk(correct=False) -> lst:
    """
    :param correct: True if you want to get a match desk
    :return: 8*2 list
    """

    while True:
        res = []
        for i in range(8):
            el = [random.randint(0, 7), random.randint(0, 7)]
            while res.count(el) > 0:
                el = [random.randint(0, 7), random.randint(0, 7)]
            res.append(el)
        if correct:
            if check(res):
                print_matrix(res)
                return res
        else:
            print_matrix(res)
            return res


def check(queens: lst) -> bool:
    """
    :param queens: 8*2 list
    :return: boolean
    """
    desk = [[True for _ in range(8)] for _ in range(8)]
    for el in queens:
        if desk[el[0]][el[1]] == True:
            desk[el[0]][el[1]] = False
            for i in range(8):
                desk[el[0]][i] = False
                desk[i][el[1]] = False
                if (el[0] + i) < 8 and (el[1] + i) < 8:
                    desk[el[0] + i][el[1] + i] = False
                if (el[0] + i) < 8 and (el[1] - i) >= 0:
                    desk[el[0] + i][el[1] - i] = False
                if (el[0] - i) >= 0 and (el[1] + i) < 8:
                    desk[el[0] - i][el[1] + i] = False
                if (el[0] - i) >= 0 and (el[1] - i) >= 0:
                    desk[el[0] - i][el[1] - i] = False
        else:
            return False
    print_matrix(queens)
    return True

print(check([[0,3],[1,6],[2,2],[3,7],[4,1],[5,4],[6,0],[7,5]]))
print(check(make_desk()))



