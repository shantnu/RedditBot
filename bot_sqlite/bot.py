'''This bot pulls replies from a sqlite table and posts them as comments on Reddit'''

from datetime import datetime
from random import randint
import sqlite3
import praw

#assumes our praw.ini is configured correctly.
REDDIT = praw.Reddit("bot1")
SUBREDDIT = REDDIT.subreddit("pythonforengineers")
#establish connection with our db, my db filename is 'bot.db'.
CONN = sqlite3.connect("bot.db")
#set row_factory to sqlite3 Row object.
CONN.row_factory = sqlite3.Row

def return_reply():
	'''Selects a random post from our sqlite db and returns a sqlite3.Row object.'''
	#create a random int to select a random record by id. If you recall we pulled
	#100 records with 'posts.py', so we will use a range from 0 - 100.
	rand_int = randint(0, 100)
	#convert rand_int to string for queries.
	rand_id = str(rand_int)
	#set table name for our queries.
	table_name = 'posts'
	#create a cursor for executing sql.
	read_cursor = CONN.cursor()
	#select an unused row to form our comment.
	read_query = 'SELECT * FROM {table} WHERE is_used = 0 AND id = ?'.format(table=table_name)
	#execute our query.
	read_cursor.execute(read_query, (rand_id,))
	#set reply as Row.
	reply = read_cursor.fetchone()
	#new cursor to write updates to 'posts'.
	write_cursor = CONN.cursor()
	#set update is_used to 1 so we know we have used this row to form content.
	#record will be filtered from our read_query in future runs.
	write_query = 'UPDATE {table} SET is_used = ? WHERE id = ?'.format(table=table_name)
	#notice the comma after 'rand.id', this sets the parameter as a single element tuple
	#so you don't confuse sqlite.
	write_cursor.execute(write_query, (1, rand_id,))
	#return our row.
	return reply

def post_comment():
	'''Posts a comment created in the return_reply function to a Reddit post.'''
	#get our reply.
	reply = return_reply()
	#string together our comment to post.
	comment = reply['self_text'] + " -" + reply['author']
	#loop through posts, limit set to 1 to avoid exceeding API rate limit.
	#using 'SUBREDDIT.new' so we don't hit archived posts
	for post in SUBREDDIT.new(limit=1):
		read = CONN.cursor()
		read_table_name = 'replied_to'
		read_query = 'SELECT * FROM {table} WHERE submission_id = ?'.format(table=read_table_name)
		read.execute(read_query, (post.id,))
		#set result.
		read_result = read.fetchone()
		print(read_result)
		#if the submission id doesn't exist in our db we post our comment.
		#this could use error handling.
		if read_result is None:
			post.reply(comment)
			confirm_message = '''Replied to: {}\nwith the comment: {}'''.format(post.title, comment)
			print(confirm_message)
			reply_time = str(datetime.now())
			#record our submission.
			write = CONN.cursor()
			write_table_name = 'replied_to'
			write_query = '''INSERT INTO {table} (time_replied, submission_id) 
			VALUES (?, ?)'''.format(table=write_table_name)
			write.execute(write_query, (reply_time, post.id))
			CONN.commit()
		#if the our read_query returns a result we have already commented on the newest post.		
		else:
			print('Nothing new ;(')
			
#main method.
def main():
	'''Main function of bot.py. Runs the post_comment function.'''
	post_comment()
#call main.
if __name__ == "__main__":
	main()
#close the connection.
CONN.close()
