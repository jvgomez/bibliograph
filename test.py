#!/usr/bin/env python
#-*- coding: utf-8 -*-

from reftypes.reference import Reference
from refsqlite.sqlitemanager import SQLiteManager
from datetime import date

# TODO: set programming style

# Get data for a new database entry from user terminal input.
#ref = Reference()
authors = [{'Name': 'Javier', 'Middle': 'V', 'Lastname': 'Gomez'},
           {'Name': 'Jorge', 'Lastname': 'Irazabal'}]

ref = Reference(label='jvgomez14', title='Fast Marching rules', date=date(year=2014,month=1,day=1), authors=authors)
#ref2 = Reference('dasanchez15', ['David Alvarez','Javier V Gomez'], 'Fast Marching rules 2', '2015')
#ref3 = Reference('dasanchez16', ['David Alvarez'], 'Fast Marching sucks', '2016')

# Giving the new data to the DB manager.
with SQLiteManager('references.db') as db:
    db.insert(ref)
    #db.insert(ref2)
    #db.insert(ref3)

    # Doing a request and saving to JSON.
   # db.query_author('Javier V Gomez')
   # JSONdoc = db.query_author_to_JSON('Javier V Gomez')
   # with open('query.json', 'w') as outfile:
   #     outfile.write(JSONdoc)
