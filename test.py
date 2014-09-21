#!/usr/bin/env python
#-*- coding: utf-8 -*-

from reftypes.reference import Reference
from refsqlite.sqlitemanager import SQLiteManager

# Get data for a new database entry from user terminal input.
#ref = Reference()
ref = Reference(['Javier V Gomez'], 'Fast Marching rules', '2014')

# Giving the new data to the DB manager.
db = SQLiteManager('references.db')
db.insert(ref)