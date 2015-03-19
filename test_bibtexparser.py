#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Javier V Gomez'
#
# # Creating test file
# bibtex = """@ARTICLE{Cesar2013,
#   author = {Jean César},
#   title = {An amazing title},
#   year = {2013},
#   month = jan,
#   volume = {12},
#   pages = {12--23},
#   journal = {Nice Journal},
#   abstract = {This is an abstract. This line should be long enough to test
#      multilines...},
#   comments = {A comment},
#   keywords = {keyword1, keyword2}
# }
# """
#
# with open('data/bibtex.bib', 'w') as bibfile:
#     bibfile.write(bibtex)
#
# # Testing
# import sys
# import os
# from pprint import pprint
# btp_path = os.path.join('.', 'python-bibtexparser')  # Creates platform-independent BibTexParser (BTP) path.
# sys.path.append(btp_path)  # Appends BTP to system path, so that next import works.
# import bibtexparser
#
# # Load bibtex file and get its content as string.
# with open('data/bibtex.bib') as bibtex_file:
#     bibtex_str = bibtex_file.read()
#
# # Parse the string.
# bib_database = bibtexparser.loads(bibtex_str)
#
# print(bib_database.entries)

import sys
import os
btp_path = os.path.join('.', 'python-bibtexparser')  # Creates platform-independent BibTexParser (BTP) path.
sys.path.append(btp_path)  # Appends BTP to system path, so that next import works.
# import bibtexparser
import logging
import logging.config

logger = logging.getLogger(__name__)

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s %(funcName)s:%(lineno)d: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'formatter': 'standard',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'formatter': 'standard',
            'propagate': True
        }
    }
})


if __name__ == '__main__':
    bibtex = """@ARTICLE{Cesar2013,
      author = {Jean César},
      title = {An amazing title},
      year = {2013},
      month = jan,
      volume = {12},
      pages = {12--23},
      journal = {Nice Journal},
      abstract = {This is an abstract. This line should be long enough to test
             multilines...},
      comments = {A comment},
      keywords = {keyword1, keyword2},
      mytag = {detected},
    }
    """

    with open('bibtex.bib', 'w') as bibfile:
        bibfile.write(bibtex)

    from bibtexparser.bparser import BibTexParser

    with open('bibtex.bib', 'r') as bibfile:
        bp = BibTexParser(bibfile.read())
        print(bp.get_entry_list())