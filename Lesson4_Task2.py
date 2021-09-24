'''
Базы данных. Урок 4. Задание 2

Написать SELECT-запросы, которые выведут информацию согласно инструкциям ниже.
Внимание! Результаты запросов не должны быть пустыми (учтите при заполнении таблиц).

    название и год выхода альбомов, вышедших в 2018 году;
    название и продолжительность самого длительного трека;
    название треков, продолжительность которых не менее 3,5 минуты;
    названия сборников, вышедших в период с 2018 по 2020 год включительно;
    исполнители, чье имя состоит из 1 слова;
    название треков, которые содержат слово "мой"/"my".
20.09.21

'''

import sqlalchemy
#import psycopg2


def sec_min(sec_in):
    minut = sec_in // 60
    sec = sec_in % 60
    sec = '{:02}'.format(sec)
    return (minut, sec)


# Создаем engine
db = 'postgresql://shuman:mocart@localhost:5432/music_box1'
engine = sqlalchemy.create_engine(db)
# Устанавливаем соединение с БД.
connection = engine.connect()

sel = connection.execute('SELECT album_name FROM Album WHERE album_year = 1984.').fetchall()
print('1. Альбомы выпущенные в 1984 году:')
for i in sel:
    print(*i)

print()
print('2. Название и продолжительность самого длительного трека.')
max_time = connection.execute('SELECT MAX(time) FROM Track ').fetchone()
name_max_time = connection.execute(f'SELECT track_name FROM Track where time = {max_time[0]}').fetchone()

max_time = sec_min(max_time[0])  # переводим секунды в мин:сек

print(f'Трек: {name_max_time[0]}, длительность: {max_time[0]}:{max_time[1]}')
print()

print('3. Название треков, продолжительность которых не менее 3,5 минуты.')
long_times = connection.execute('SELECT time, track_name FROM Track WHERE time >= 210').fetchall()

for i in long_times:
    track_time = sec_min(i[0])
    print(f'Трек: {i[1]}, длительность: {track_time[0]}:{track_time[1]}')
print()

print('4. Названия сборников, вышедших в период с 2018 по 2020 год включительно.')
sel = connection.execute('SELECT mix_name, year FROM Mix WHERE year BETWEEN 2018 AND 2020').fetchall()
for i in sel:
    print(f'Альбом: {i[0]}, год выпуска: {i[1]}')
print()

print('5. Исполнители, чье имя состоит из 1 слова.')
sel = connection.execute('SELECT musician_name FROM musician').fetchall()
for i in sel:
    if ' ' not in i[0].strip():
        print(i[0])
print()

print('6. Название треков, которые содержат слово "я"/"me".')
sel = connection.execute("""SELECT track_name FROM Track WHERE track_name iLIKE 'me %%'
 OR track_name iLIKE '%% me %%' OR track_name iLIKE '%% me' OR track_name iLIKE 'я %%'
 OR track_name iLIKE '%% я %%' OR track_name iLIKE '%% я'""").fetchall()
for i in sel:
    print(i[0])