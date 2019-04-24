#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random


class Game:
    number_list: list

    def __init__(self, start=0):
        self.number_list: list = list(range(1, 91))
        random.shuffle(self.number_list)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.number_list) > 0:
            return self.number_list.pop(0)
        else:
            range
            StopIteration


class Card:
    line1: list
    line2: list
    line3: list
    full_list: list

    def __init__(self):
        self.full_list = list(range(1, 91))
        random.shuffle(self.full_list)
        self.full_list = self.full_list[0:15]
        self.line1 = self.full_list[0:5]
        self.line2 = self.full_list[5:10]
        self.line3 = self.full_list[10:15]
        for i in range(3):
            self.full_list.insert(random.randint(0, 5), ' ')
            self.full_list.insert(random.randint(8, 13), ' ')
            self.full_list.insert(random.randint(16, 21), ' ')
    def mark_number(self, number):
        if number in self.full_list:
            self.full_list[self.full_list.index(number)] = '-'
            if number in self.line1:
                self.line1[self.line1.index(number)] = 0
            if number in self.line2:
                self.line2[self.line2.index(number)] = 0
            if number in self.line3:
                self.line3[self.line3.index(number)] = 0

    def check_number(self, number):
        if number in self.full_list:
            return True
        else:
            return False

    def check_card(self):
        if sum(self.line1) == 0 or sum(self.line2) == 0 or sum(self.line3) == 0:
            return True
        else:
            return False

    def print_card(self):
        align = list(map(len, map(str, self.line1)))

        def make_line(seq, aligns):
            return ' '.join('{0:>{1}}'.format(i, j) for i, j in zip(seq, aligns))

        m1 = make_line(self.full_list[0:8], [3, 3, 3, 3, 3, 3, 3, 3])
        m2 = make_line(self.full_list[8:16], [3, 3, 3, 3, 3, 3, 3, 3])
        m3 = make_line(self.full_list[16:24], [3, 3, 3, 3, 3, 3, 3, 3])

        out = '\n'.join((m1, m2, m3))
        print(out)


card1 = Card()
card2 = Card()
new_game = Game()
for x in new_game:
    print('---------- Your card ----------')
    card1.print_card()
    print('--------------------------------')
    print('-------  Computer''s card --------')
    card2.print_card()
    print('--------------------------------')
    print('New barrel: ', x)
    if input('Mark the number on your card? (y/n)') == 'y':
        if card1.check_number(x):
            card1.mark_number(x)
        else:
            print('YOU LOSE!!!')
            break
    else:
        if card1.check_number(x):
            print('YOU LOSE!!!')
            break

    card2.mark_number(x)

    if card1.check_card() and card2.check_card():
        print('DRAW!!!')
        break
    elif card1.check_card():
        print('YOU WIN!!!')
        break
    elif card2.check_card():
        print('YOU LOSE!!! COMPUTER WIN!!!')
        break
