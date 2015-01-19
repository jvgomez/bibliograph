import os
from pprint import pprint
import sqlite3
import json
import itertools
from sqlitedefinitions import *

# TODO: include article type in DB

class SQLiteManager:
    def __init__(self, db_name='default.db'):
        self.db_name = db_name

    def __enter__(self):

        class SQLiteObject:

            def __init__(self, db_name):
                if os.path.isfile(db_name):
                    os.remove(db_name)
                self.conn = sqlite3.connect(db_name)
                self.conn.isolation_level = None
                self.c = self.conn.cursor()

                # Create table
                self.c.execute(CREATE_ARTICLES_TABLE)
                self.c.execute(CREATE_AUTHORS_TABLE)
                self.c.execute(CREATE_AIA_TABLE)
                self.c.execute(CREATE_REFERENCES_TABLE)

                self.conn.commit()

                self.col_names = ['id', 'type', 'main_author', 'author2', 'author3', 'author4',
                                  'et_al', 'title', 'year']

            def insert(self, ref):
                """
                :type ref: reftypes.reference.Reference
                """
                self.c.execute('INSERT INTO ARTICLES (Title, Date, Label) VALUES (?,?,?)',
                               [ref.title, ref.date.isoformat(), ref.label])
                id_article = self.c.lastrowid

                matrix = [[author['Name'], author.get('Middle'), author['Lastname']] for author in ref.authors]
                self.c.executemany('INSERT INTO AUTHORS (Name, Middle, Lastname) VALUES (?,?,?)', matrix)
                id_authors = self.c.execute('SELECT ID FROM AUTHORS ORDER BY ID DESC LIMIT 1').fetchone()[0] + 1
                id_authors = range(id_authors-len(ref.authors), id_authors)

                matrix = zip([id_article]*len(id_authors),id_authors)
                self.c.executemany('INSERT INTO AuthorsInArticles (Article, Author) VALUES (?,?)', matrix)

            def query_author(self, name):#todo. doesn't work!!!!
                query = '''SELECT * FROM refs WHERE
                    main_author=\'{0}\' or author2=\'{0}\' or author3=\'{0}\' or author4=\'{0}\''''.format(name)

                self.c.execute(query)
                return self.c.fetchall()

            def query_author_to_JSON(self, name):
                entries = self.query_author(name)
                entries_as_dict = {}
                for entry in entries:
                    entries_as_dict[entry[0]] = dict(itertools.izip(self.col_names, entry))

                return json.dumps(entries_as_dict)

            def cleanup(self):
                self.conn.close()

        self.sqlite_obj = SQLiteObject(self.db_name)
        return self.sqlite_obj

    def __exit__(self, type, value, traceback):
        self.sqlite_obj.cleanup()

