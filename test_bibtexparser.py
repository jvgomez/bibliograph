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

logger = logging.getLogger(__name__)
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
G = nx.DiGraph()  # Directed graph_ children -> parent
for entry in bib_database.get_entry_list():
    if entry['ID'] in G:
        print(Fore.YELLOW + Style.BRIGHT +
              "[Warning] - Entry with ID \"{0}\" already exists. Ignored."
              .format(entry['ID']))
    else:
        G.add_node(entry['ID'], entry)

# Creating edges between ID and relations IDs.
# Edges are in 'upward' direction, that is, children point to their parent.
for ID in G.nodes():  # For each node with relations field...
    if 'relations' in G.node[ID]:
        for rel in G.node[ID]['relations']:  # ... for each relation...
            if rel in G:  # ... look for and link to the corresponding parent
                logger.debug("{0} linked to {1}".format(G.node[ID]['ID'], rel))
                G.add_edge(G.node[ID]['ID'], rel)
            else:  # NetworkX can create automatically the nonexistent node, but we do not
                # want that, since it would be empty, only with name.
                print(Fore.YELLOW + Style.BRIGHT +
                      "[Warning] - Entry \"{0}\" links to nonexistent entry \"{1}\". Ignored"
                      .format(G.node[ID]['ID'], rel))

# Plotting
# TODO in the future it might be better to use Graphviz (better plotting options)

import matplotlib.pyplot as plt

pos = nx.spring_layout(G)
fig = plt.figure(facecolor='white')
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.axis('off')
plt.show()
# plt.savefig("graph.png")


# Plotting using D3 and force template.
import json
from networkx.readwrite import json_graph
from server.StopableHTTPServer import load_url

# Create and save json
json_file = 'data/graph.json'
d = json_graph.node_link_data(G)  # node-link format to serialize
with open(json_file, 'w') as jsonfile:
    json.dump(d, jsonfile)
    logger.debug('Wrote node-link JSON data to {0}'.format(json_file))

# open URL in running web browser
load_url('data/force.html')