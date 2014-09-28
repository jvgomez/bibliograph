#!/usr/bin/env python
#-*- coding: utf-8 -*-

from reftypes.reference import Reference
from refsqlite.sqlitemanager import SQLiteManager

# Get data for a new database entry from user terminal input.
#ref = Reference()
ref = Reference('jvgomez14', ['Javier V Gomez'], 'Fast Marching rules', '2014')
ref2 = Reference('dasanchez15', ['David Alvarez','Javier V Gomez'], 'Fast Marching rules 2', '2015')
ref3 = Reference('dasanchez16', ['David Alvarez'], 'Fast Marching sucks', '2016')

# Giving the new data to the DB manager.
with SQLiteManager('references.db') as db:
    db.insert(ref)
    db.insert(ref2)
    db.insert(ref3)

    # Doing a request and saving to JSON.
    db.query_author('Javier V Gomez')
    JSONdoc = db.query_author_to_JSON('Javier V Gomez')
    with open('query.json', 'w') as outfile:
        outfile.write(JSONdoc)