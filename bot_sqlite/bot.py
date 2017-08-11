'''This bot pulls replies from a sqlite table and posts them as comments on Reddit'''

from datetime import datetime
from random import randint
import sqlite3
import praw
#assumes our praw.ini is configured correctly
REDDIT = praw.Reddit("bot1")
SUBREDDIT = REDDIT.subreddit("pythonforengineers")
CONN = sqlite3.connect("bot.db")
#set row_factory to sqlite Row object
CONN.row_factory = sqlite3.Row

def return_reply():
	'''Selects a random post from our sqlite db and returns a sqlite3.Row object.'''
	#create random int to select a random record by id
	rand_int = randint(0, 100)
	#convert to string for query
	rand_id = str(rand_int)
	#create our cursor for executing sql
	cursor = CONN.cursor()
	#form our query
	table_name = 'posts'
	query = 'SELECT * FROM {table} WHERE is_used = 0 AND id = {id}'.format(table=table_name, id=rand_id)
	#execute our query
	cursor.execute(query)
	#set reply as Row
	reply = cursor.fetchone()
	return reply

def post_comment():
	'''Posts a comment created in the return_reply function to a Reddit post.'''
	#gets our reply
	reply = return_reply()
	#string together our comment
	comment = reply['self_text'] + " -" + reply['author']
	for post in SUBREDDIT.new(limit=1):
		read = CONN.cursor()
		table_name = 'replied_to'
		sub_id = 'submission_id'
		read_query = 'SELECT ? FROM {table} WHERE submission_id = ?'.format(table=table_name)
		#notice the comma after 'post.id', this sets the parameter as a single element tuple
		#so you don't confuse sqlite
		read.execute(read_query, (sub_id, post.id,))
		#fetch result
		read_result = read.fetchone()
		#if their submission doesn't exist in the db we post our comment
		#this needs error handling, fork it and fix it!
		if read_result is None:	
			reply_time = str(datetime.now())
			write = CONN.cursor()
			write_table_name = 'replied_to'
			write_query = '''INSERT INTO {table} (time_replied, submission_id) 
			VALUES (?, ?)'''.format(table=write_table_name)
			write.execute(write_query, (reply_time, post.id))
			CONN.commit()
			#here is the magic!
			post.reply(comment)
			confirm_message = '''You have succesfully replied to the post titled: {} with the comment: {}'''.format(post.title, comment)
			print(confirm_message)
			
#main method
def main():
	'''Main function of bot.py. Runs the post_comment function.'''
	post_comment()
#call main
if __name__ == "__main__":
	main()
#close the connection
CONN.close()
