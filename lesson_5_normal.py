# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из __easy.py

import lesson_5_easy as easy

if __name__ == '__main__':
    while True:
        print('1. Change dir')
        print('2. Browse dir')
        print('3. Delete dir')
        print('4. Create dir')
        print('5. Exit')
        user_choice = input('Choose option: ')
        if user_choice == '1':
            easy.mychdir(input('Enter the way: '))
        elif user_choice == '2':
            easy.mylistdir()
        elif user_choice == '3':
            easy.myrmdir(input('Enter the name: '))
        elif user_choice == '4':
            easy.mymkdir(input('Enter the name: '))
        elif user_choice == '5':
            break
        else:
            print('Invalid input')
