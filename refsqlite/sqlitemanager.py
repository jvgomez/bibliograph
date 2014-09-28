import os
import sqlite3
import json
import itertools

class SQLiteManager:

    def __init__(self, db_name = 'default.db'):
        self.db_name = db_name

    def __enter__(self):

        class SQLiteObject:

            def __init__(self, db_name):
                if os.path.isfile(db_name):
                    os.remove(db_name)
                self.conn = sqlite3.connect(db_name)
                self.c = self.conn.cursor()

                # Create table
                self.c.execute('''CREATE TABLE IF NOT EXISTS refs
                    (id text, type int, main_author text, author2 text, author3 text, author4 text, et_al int, title text, year int)''')

                self.col_names = ['id', 'type', 'main_author','author2', 'author3', 'author4',
                                  'et_al', 'title', 'year']


            def insert(self, ref):
                new_entry = [ref.id, ref.ref_type, ref.authors[0], ref.authors[1], 
                             ref.authors[2], ref.authors[3], ref.et_al, ref.title, ref.year]
                # Insert a row of data
                self.c.execute('INSERT INTO refs VALUES (?,?,?,?,?,?,?,?,?)', new_entry)

                # Save (commit) the changes.
                self.conn.commit()
            
            def query_author(self, name):
                query = '''SELECT * FROM refs WHERE
                    main_author=\'{0}\' or author2=\'{0}\' or author3=\'{0}\' or author4=\'{0}\''''.format(name)

                self.c.execute(query)
                return self.c.fetchall();

            def query_author_to_JSON(self,name):
                entries = self.query_author(name)
                entries_as_dict = {}
                for entry in entries:
                    entries_as_dict[entry[0]] = dict(itertools.izip(self.col_names,entry))

                return json.dumps(entries_as_dict)

            def cleanup(self):
                self.conn.close()

        self.sqlite_obj = SQLiteObject(self.db_name)
        return self.sqlite_obj

    def __exit__(self, type, value, traceback):
        self.sqlite_obj.cleanup()

