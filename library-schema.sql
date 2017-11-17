-- sqlite3 library.db < library-schema.sql
--to add the path
--PATH=%PATH%;C:\SQLite

--The DROP TABLE statement is used to drop an existing table in a database
--The CREATE TABLE statement is used to create a new table in a database
--The PRIMARY KEY constraint uniquely identifies each record in a database table
--The NOT NULL constraint enforces a column to NOT accept NULL values
--Autoincrement allows a unique number to be generated automatically when a new record is inserted into a table
--The EXISTS operator returns true if the subquery returns one or more records

drop table if exists country;
--If a table with the name country exists in the database, drop it
create table country (
    id integer primary key autoincrement,
    name text not null
);

drop table if exists author;
create table author (
    id integer primary key autoincrement,
    country_id integer,
    name text not null
);

drop table if exists book;
create table book (
    id integer primary key autoincrement,
    author_id integer,
    title text not null,
    isbn text
);








