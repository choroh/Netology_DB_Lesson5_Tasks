insert into stile (stile_name) values
('Rock'),
('Blues'),
('Disko'),
('Jazz'),
('Classic');

insert into musician (musician_name) values
('Deep Purple'),
('Rainbow'),
('Pink Floyd'),
('Scorpions'),
('Abba'),
('Gary Moore'),
('Secret Service'),
('Петр Чайковский');

insert into musician_stile values
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 3),
(6, 1),
(6, 2),
(7, 3),
(8, 5);

insert into album (album_name, album_year) values
('Made In Japan', 1972),
('Bent Out of Shape', 1983),
('Wish You Were Here', 1975),
('Taken by Force', 1977),
('Super Trouper', 1980),
('Still Got The Blues', 1990),
('Jupiter Sign', 1984),
('Концерт для фортепиано с оркестром', 2001);

insert into musician_album values
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8);

insert into track (track_name, time, album_id) values
('Highway Star', 412, 1),
('Child In Time', 745, 1),
('Smoke On The Water', 452, 1),
('The Mule', 590, 1),
('Strange Kind Of Woman', 576, 1),
('Lazy', 651, 1),
('Space Truckin', 1182, 1);

insert into track (track_name, time, album_id) values
('Stranded', 270, 2),
('Can''t Let You Go', 262, 2),
('Fool For The Night', 244, 2),
('Fire Dance', 270, 2),
('Anybody There', 160, 2),
('Desperate Heart', 276, 2),
('Street Of Dreams', 266, 2),
('Drinking With The Devil', 224, 2),
('Snowman', 297, 2),
('Make Your Move', 265, 2);

insert into track (track_name, time, album_id) values
('Wish You Were Here', 293, 3),
('Another Brick In The Wall II', 198, 3),
('Proper Education', 213, 3),
('Another Brick In The Wall I', 360, 3),
('Money', 283, 3),
('Us And Them', 462, 3),
('Hey You', 281, 3),
('Is There Anybody Out There', 226, 3),
('Comfortably Num', 413, 3),
('Marooned', 325, 3);


insert into track (track_name, time, album_id) values
('Steamrock Fever', 217, 4),
('We''ll Burn the Sky', 386, 4),
('I''ve Got to Be Free', 240, 4),
('The Riot of Your Time', 249, 4),
('The Sails of Charon', 263, 4),
('Your Light', 271, 4),
('He''s a Woman — She''s a Man', 195, 4),
('Born to Touch Your Feelings', 460, 4),
('Suspender Love',  200, 4),
('Polar Nights', 416, 4);

insert into track (track_name, time, album_id) values
('Super Trouper', 253, 5),
('The Winner Takes It All', 295, 5),
('On And On And On', 221, 5),
('Andante, Andante', 278, 5),
('Me And I', 293, 5),
('Happy New Year', 277, 5),
('Our Last Summer', 258, 5),
('The Piper', 205, 5),
('Lay All Your Love On Me', 273, 5),
('The Way Old Friends Do', 173, 5);

insert into track (track_name, time, album_id) values
('Moving On', 158, 6),
('Oh Pretty Woman',	264, 6),
('Walking By Myself', 176, 6),
('Still Got The Blues', 368, 6),
('Texas Strut', 290, 6),
('Too Tired', 169, 6),
('King Of The Blues', 274, 6),
('As The Years Go Passing By', 462, 6),
('Midnight Blues', 297, 6),
('That Kind Of Woman', 268, 6),
('All Of Your Love', 219, 6),
('Stop Messin'' Around', 232, 6);

insert into track (track_name, time, album_id) values
('Jupiter Sign', 292, 7),
('Love Cannot Be Wrong', 173, 7),
('Visions Of You', 193, 7),
('Heart Companion', 186, 7),
('Jo-Anne, Jo-Anne',  219, 7),
('Do It', 213, 7),
('Night Cafe', 200, 7),
('All I Wanna do', 215, 7),
('Will You Be Near Me', 251, 7),
('Mrs. Marple', 214, 7);

insert into track (track_name, time, album_id) values
('Allegro non troppo e molto maestoso', 1057, 8),
('Andantino semplice', 352, 8),
('Allegro con fuoco', 366, 8);


insert into Mix  (mix_name, year) values
('Rock collection 1', 2015),
('Rock collection 2', 2016),
('Rock collection 3', 2017),
('Rock collection 4', 2018),
('Love musuc', 2018),
('Сборник медленной музыки', 2019),
('Любимые песни', 2019),
('Greatest Hits', 2020);

insert into mix_track (track_id, mix_id) values
(1, 1),
(8, 1),
(46, 1),
(23, 1),
(48, 1),
(60, 1),
(2, 1),
(3, 2),
(9, 2),
(39, 2),
(20, 2),
(29, 2),
(49, 2),
(61, 2),
(4, 2),
(5, 3),
(10, 3),
(40, 3),
(21, 3),
(30, 3),
(50, 3),
(62, 3),
(5, 3),
(6, 4),
(11, 4),
(41, 4),
(22, 4),
(31, 4),
(53, 4),
(63, 4),
(7, 4),
(34, 5),
(36, 5),
(58, 5),
(61, 5),
(9, 5),
(26, 5),
(49, 5),
(68, 5),
(12, 6),
(16, 6),
(29, 6),
(38, 6),
(51, 6),
(56, 6),
(66, 6),
(68, 6),
(61, 6),
(1, 7),
(12, 7),
(17, 7),
(19, 7),
(33, 7),
(42, 7),
(50, 7),
(69, 7),
(2, 8),
(3, 8),
(8, 8),
(16, 8),
(23, 8),
(33, 8),
(38, 8),
(44, 8);

