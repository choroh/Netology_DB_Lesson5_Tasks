create table if not exists Stile(
stile_id serial primary key,
stile_name varchar(30) not null unique
);

create table if not exists Musician(
musician_id serial primary key,
musician_name varchar(20) not null
);

create table if not exists Album(
album_id serial primary key,
album_name varchar(40) not null,
album_year integer check(album_year > 1900 and album_year < 2100)
);

create table if not exists Track(
track_id serial primary key,
track_name varchar(30) not null,
time integer check(time > 0  and time < 3600),
album_id integer references Album(album_id)
);

create table if not exists Mix(
mix_id serial primary key,
mix_name varchar(40) not null,
year integer check(year > 1900 and year < 2100)
);

create table if not exists Musician_album(
musician_id integer references Musician(musician_id),
album_id integer references Album(album_id)
);


create table if not exists Musician_stile(
musician_id integer references Musician(musician_id),
stile_id integer references Stile(stile_id)
);

create table if not exists Mix_track(
track_id integer references Track(track_id),
mix_id integer references Mix(mix_id)
);