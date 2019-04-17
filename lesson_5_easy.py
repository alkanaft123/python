# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

from os import path, mkdir, rmdir, listdir, chdir
from sys import argv
from shutil import copy


def mychdir(dir: str):
    if path.exists(dir):
        chdir(dir)
        print(f'Current dir: {dir}')
    else:
        print('This way does not exist')

def mylistdir(dir: str=None) -> list:
    for el in listdir():
        if path.isdir(el):
            print(el)


def myrmdir(dir: str):
    if path.exists(dir):
        rmdir(dir)
    else:
        print('This way does not exist')


def mymkdir(dir: str):
    mkdir(dir)

if __name__ == '__main__':
    for i in range(9):
        if not path.exists('dir_' + str(i)):
            mymkdir('dir_' + str(i))
        myrmdir('dir_' + str(i))

#
# # Задача-2:
# # Напишите скрипт, отображающий папки текущей директории.
#
    mylistdir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

    copy(argv[0], argv[0] + '_copy')
