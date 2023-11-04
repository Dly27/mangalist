import sqlite3

conn = sqlite3.connect("manga.db")

# create cursor
cur = conn.cursor()

# test data
manga_list = ("One Piece", "Naruto", "Attack on Titan", "Death Note",
         "Fullmetal Alchemist", "Dragon Ball",
         "One Punch Man", "Bleach")


table_name = "manga"
column_name = "title"

# SQL statement to delete all rows in the table
delete_query = f"DELETE FROM {table_name}"

# Execute the DELETE statement
cur.execute(delete_query)


cur.close()
conn.close()
