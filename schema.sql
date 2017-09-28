drop table if exists request_count;
create table request_count(
id integer primary key autoincrement,
name text not null,
count integer not null
);
