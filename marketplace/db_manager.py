import sqlite3
import datetime
from sqlite3 import Error

def create_connection(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file)
	except Error as e:
		print(e)

	return conn


def select_all_tasks(conn):
	cur = conn.cursor()
	cur.execute("SELECT * FROM channels_channel")

	rows = cur.fetchall()

	for row in rows:
		print(row)

def clean_channels(conn):
	cur = conn.cursor()
	cur.execute("DELETE FROM channels_channel WHERE pub_date < DATETIME('NOW', '-10 minutes')")

def main():
	database = "db.sqlite3"

	# create a database connection
	conn = create_connection(database)
	with conn:
		clean_channels(conn)

if __name__ == '__main__':
	main()