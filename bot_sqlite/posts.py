#These are doc strings, use them :)
'''Gets Reddit posts and saves selected values to a sqlite db.'''
import sqlite3
import praw
#assumes our praw.ini is configured correctly.
REDDIT = praw.Reddit('bot1')
SUBREDDIT = REDDIT.subreddit('pythonforengineers')
#establish connection with our db.
CONN = sqlite3.connect("bot.db")

def db_insert():
	'''Pull posts from Reddit and insert into a sqlite table.'''
	#this should look familiar
	for post in SUBREDDIT.hot(limit=100):	
		cursor = CONN.cursor()
		#setting a value on null self.text, this way we can fill our db.
		#we can also use an if statement to filter out null self.text values.
		#give it a try!
		if (post.selftext == ""):
			post.selftext = post.author.name + " didn't add self text, how lazy."
		#we set our table name and query as a variable to avoid sql injection.
		#although that shouldn't be a concern here we should still write it correctly
		#to instill good habits.
		table_name = 'posts'
		query = '''INSERT INTO {table} (submission_id, self_text, title, author, score, content_url, is_used) 
		VALUES (?, ?, ?, ?, ?, ?, ?)'''.format(table=table_name)
		#execute our query
		cursor.execute(query, (post.id, post.selftext, post.title, post.author.name, post.score, post.url, 0))
		#commit changes to the db
		CONN.commit()
		#print some values to verify successful read
		print("Title: {}".format(post.title))
		print("Text: {}".format(post.selftext))
		print("Score: {}".format(post.score))
		print("---------------------------------")
#main method
def main():
	'''Main function of posts.py - Runs the db_insert function.'''
	db_insert()
#call main
if __name__ == "__main__":
	main()
#close the connection
CONN.close()