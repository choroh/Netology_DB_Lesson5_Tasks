"""
Netology
Базы данных. Занятие 5.
Написать SELECT-запросы, которые выведут информацию согласно инструкциям ниже.
Внимание! Результаты запросов не должны быть пустыми (при необходимости добавьте данные в таблицы).

    количество исполнителей в каждом жанре;
    количество треков, вошедших в альбомы 2019-2020 годов;
    средняя продолжительность треков по каждому альбому;
    все исполнители, которые не выпустили альбомы в 2020 году;
    названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
    название альбомов, в которых присутствуют исполнители более 1 жанра;
    наименование треков, которые не входят в сборники;
    исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
    название альбомов, содержащих наименьшее количество треков.
23.09.21
"""


#  Перевод секунд в минуты : секунды
def sec_min(sec_in):
    minut = sec_in // 60
    sec = sec_in % 60
    sec = '{:02}'.format(sec)
    return (minut, sec)


import psycopg2
import sqlalchemy

db = 'postgresql://shuman:mocart@localhost:5432/music_box1'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

print('1. Количество исполнителей в каждом жанре')
sel = connection.execute("""SELECT stile_name, COUNT(musician_id) FROM stile 
    JOIN musician_stile ON stile.stile_id = musician_stile.stile_id
    GROUP BY stile_name;""").fetchall()
for i in sel:
    print(f'В стиле: {i[0]} {i[1]} исполнителей.')
print()

print('2. Количество треков, вошедших в альбомы 1972-1975 годов')
sel = connection.execute("""SELECT COUNT(track_name) FROM track
    JOIN album ON track.album_id = album.album_id
    WHERE album.album_year BETWEEN 1972 AND 1975;""").fetchone()
print(f'В альбомы 1972-1975 годов вошли {sel[0]} песен.')
print()

#  средняя продолжительность треков по каждому альбому;
print('3. Средняя продолжительность треков по каждому альбому')
sel = connection.execute("""SELECT album_name, ROUND(AVG(time)) FROM album
    JOIN track ON album.album_id = track.album_id
    GROUP BY album.album_name
    ORDER BY ROUND(AVG(time)) DESC;""").fetchall()
for i in sel:
    print(f'"{i[0]}" - {sec_min(i[1])[0]} : {sec_min(i[1])[1]}')
print()

print('4. Все исполнители, которые не выпустили альбомы в 1990 году')
sel = connection.execute("""SELECT musician_name FROM musician
    JOIN musician_album ON musician.musician_id = musician_album.musician_id
    JOIN album ON musician_album.album_id = album.album_id
    WHERE album.album_year != 1990
    ORDER BY musician;
    """).fetchall()
for i in sel:
    print(f'{i[0]}')
print()

print('5. Названия сборников, в которых присутствует исполнитель Deep Purple')
sel = connection.execute("""SELECT mix_name FROM mix
    JOIN mix_track ON mix.mix_id = mix_track.mix_id
    JOIN track ON mix_track.track_id = track.track_id
    JOIN album ON track.album_id = album.album_id
    JOIN musician_album ON album.album_id = musician_album.album_id
    JOIN musician ON musician_album.musician_id = musician.musician_id
    WHERE musician.musician_name IN ('Deep Purple')
    GROUP BY mix_name
    ORDER BY mix_name;
    """).fetchall()
for i in sel:
    print(f'"{i[0]}"')
print()

print('6. Название альбомов, в которых присутствуют исполнители более 1 жанра.')
sel = connection.execute("""SELECT album_name, musician_name, COUNT(stile_name) FROM album
    JOIN musician_album ON album.album_id = musician_album.album_id
    JOIN musician ON musician_album.musician_id = musician.musician_id
    JOIN musician_stile ON musician.musician_id = musician_stile.musician_id
    JOIN stile ON musician_stile.stile_id = stile.stile_id
    GROUP BY album_name, musician_name
    HAVING COUNT(stile_name) > 1;
    """).fetchall()
for i in sel:
    print(f'В альбоме "{i[0]}" исполнитель {i[1]} присутствует в {i[2]} жанрах')
print()

print('7. Наименование песен, которые не входят в сборники.')
sel = connection.execute("""SELECT track_name FROM track
    LEFT JOIN  mix_track ON track.track_id = mix_track.track_id
    WHERE mix_track.track_id IS NULL
    ORDER BY track_name;
    """).fetchall()
for i in sel:
    print(i[0])
print()

print('8. Исполнители, написавшие самый короткий по продолжительности трек.')
sel = connection.execute("""
    SELECT musician_name, time FROM musician
    JOIN musician_album ON musician.musician_id = musician_album.musician_id
    JOIN album ON musician_album.album_id = album.album_id
    JOIN track ON album.album_id = track.album_id
    WHERE time = (SELECT MIN(time) FROM track)
    GROUP BY musician_name, time;
    """).fetchall()
for i in sel:
    print(f'Самый короткий по продолжительности трек у исполнителя: {i[0]} - {sec_min(i[1])[0]} : {sec_min(i[1])[1]}')
print()

print('9. Название альбомов, содержащих наименьшее количество треков.')
sel = connection.execute("""
    SELECT album_name, COUNT(track) FROM album
    JOIN track ON album.album_id = track.album_id
    GROUP BY album_name
    HAVING COUNT(track) = (
        SELECT COUNT(track) FROM album
        JOIN track ON album.album_id = track.album_id
        GROUP BY album_name
        ORDER BY COUNT(track)
        LIMIT 1)
        """).fetchall()
for i in sel:
    print(f'{i[0]}, {i[1]} композиций')
