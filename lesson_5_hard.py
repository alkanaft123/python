# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print


def cp(name : str = None):
    if name != None:
        shutil.copy(os.getcwd() + '\\' + name, os.getcwd() + '\\' + os.path.splitext(name)[0] + '_copy.txt')



def rm(name: str = None):
    if name != None:
        if os.path.exists(name):
            if input('Are you sure? (y\\n)') == 'y':
                os.remove(name)
            else:
                print('Removing was canceled!')
        else:
            print('Sorry. this way does not exist')

# от этой команды мало толку, так как в мейне нет цикла, который бы позволил
# продолжить делать что-то в другой директории (такой цикл я делал), а так ну поменяли и поменяли,
# выполнение скрипта завершилось и что дальше

def cd(name):
    if name != None:
        os.chdir(name)


def ls():
    print(os.getcwd())


if __name__ == '__main__':

    do = {
        "help": print_help,
        "mkdir": make_dir,
        "ping": ping,
        "cp": cp,
        "rm": rm,
        "cd": cd,
        "ls": ls,
    }

    args = {
        "help": 1,
        "mkdir": 2,
        "ping": 1,
        "cp": 2,
        "rm": 2,
        "cd": 2,
        "ls": 1,
    }

    try:
        dir_name = sys.argv[2]
    except IndexError:
        dir_name = None

    try:
        key = sys.argv[1]
    except IndexError:
        key = None

    if key:
        if do.get(key):
            if args[key] == 2:
                do[key](dir_name)
            else:
                do[key]()
        else:
            print("Задан неверный ключ")
            print("Укажите ключ help для получения справки")
