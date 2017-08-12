--you can name the table however you like, just replace 'posts' or'replied_to'
--feel free to add columns and store whatever data you like
create table posts (
	id integer not null primary key autoincrement,
	submission_id text not null,
	self_text text not null,
	title text not null,
	author text not null,
	score text not null,
	content_url text not null,
	is_used integer not null
);
create table replied_to (
	id integer not null primary key autoincrement,
	time_replied date not null,
	submission_id text not null
);
--run these commands in the directory where the db is stored
--$sqlite3 your_db.db
--sqlite> .read bot.sql
--sqlite> .tables
-- HOORAY! you have tables!