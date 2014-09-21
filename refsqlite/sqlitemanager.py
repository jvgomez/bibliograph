import os
import sqlite3

class SQLiteManager:

    def __init__(self, db_name = 'default.db'):
        if os.path.isfile(db_name):
            os.remove(db_name)
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

        # Create table
        self.c.execute('''CREATE TABLE refs
                    (type int, main_author text, author2 text, author3 text, author4 text, et_al int, title text, year int)''')


    def insert(self, ref):
        new_entry = [ref.ref_type, ref.authors[0], ref.authors[1], 
                     ref.authors[2], ref.authors[3], ref.et_al, ref.title, ref.year]
        # Insert a row of data
        self.c.execute('INSERT INTO refs VALUES (?,?,?,?,?,?,?,?)', new_entry)

        # Save (commit) the changes and close.
        self.conn.commit()
        self.conn.close()