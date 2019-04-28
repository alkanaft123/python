""" OpenWeatherMap (экспорт)
Сделать скрипт, экспортирующий данные из базы данных погоды,
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.
Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]

При выгрузке в html можно по коду погоды (weather.id) подтянуть
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions
Экспорт происходит в файл filename.
Опционально можно задать в командной строке город. В этом случае
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.
"""

import csv
import json
import sqlite3
from sys import argv


def csv_writer(data, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


def json_writer(data, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for el in data:
            writer.writerow(el)


def html_writer(data, path):
    pass


if __name__ == '__main__':
    conn = sqlite3.connect("mydatabase.db")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cities")

    if len(argv) > 1:
        if argv[1] == '--csv':
            csv_writer(cursor.fetchall(), argv[2])
        elif argv[1] == '--json':
            json_writer(cursor.fetchall(), argv[2])
        elif argv[1] == '--html':
            pass
        else:
            print(cursor.fetchall())
