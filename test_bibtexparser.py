#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Javier V Gomez'

from pprint import pprint
import sys
import os
btp_path = os.path.join('.', 'python-bibtexparser')  # Creates platform-independent BibTexParser (BTP) path.
sys.path.append(btp_path)  # Appends BTP to system path, so that next import works.
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *
import networkx as nx

import re
from colorama import *
init(autoreset=True)
import logging
import logging.config

# logger = logging.getLogger(__name__)
# logging.config.dictConfig({
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'standard': {
#             'format': '%(asctime)s [%(levelname)s] %(name)s %(funcName)s:%(lineno)d: %(message)s'
#         },
#     },
#     'handlers': {
#         'default': {
#             'level': 'DEBUG',
#             'formatter': 'standard',
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         '': {
#             'handlers': ['default'],
#             'level': 'DEBUG',
#             'formatter': 'standard',
#             'propagate': True
#         }
#     }
# })


# TODO contribute this function to bibtexparser
def split_custom_field(record, field, sep=',|;'):
    """
    Split a custom field into a list.

    :param record: the record.
    :type record: dict
    :param field: key of the field to split.
    :type record: string
    :param sep: pattern used for the splitting regexp.
    :type record: string, optional
    :returns: dict -- the modified record.

    """
    if field in record:
        record[field] = [i.strip() for i in re.split(sep, record[field].replace('\n', ''))]

    return record


# Defining my customizations: split keywords and relations in a list.
def my_customizations(record):
    record = keyword(record)
    record = split_custom_field(record, 'relations')
    return record

# Parsing bibtex file and getting a dictionary
with open('data/bibtex.bib', 'r') as bibfile:
    parser = BibTexParser()
    parser.customization = my_customizations
    bib_database = bibtexparser.load(bibfile, parser=parser)

bib_dict = bib_database.get_entry_dict()

# Creating nodes
G = nx.Graph()
for entry in bib_database.get_entry_list():
    if entry['ID'] in G:
        print(Fore.YELLOW + Style.BRIGHT + "[Warning] - Entry with ID \"{0}\" already exists.".format(entry['ID']))
    else:
        G.add_node(entry['ID'], entry)

# Creating edges
for ID in G.nodes():
    if 'relations' in G.node[ID]:
        print G.node[ID]['relations']

# import matplotlib.pyplot as plt
# nx.draw(G)
# plt.show()
# #plt.savefig("graph.png")

# TODO test javascript support