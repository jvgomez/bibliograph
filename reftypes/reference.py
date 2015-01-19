class Reference:
    def terminalInit(self):
        types = {1: self.create_journal,
                 2: self.create_conference,
                 3: self.create_book,
                 4: self.create_default
        }

        self.label = raw_input('ID: ')
        self.type = int(raw_input('Type of article (1 journal, 2 conf, 3 book, 4 other): '))
        types[self.type]()

    # Overloaded constructor for specific type (now default).
    # TODO: add type checking and error handling (and so).
    def __init__(self, label=None, authors=None, title=None, date=None, type=4):
        if label is None:
            self.terminalInit()
        else:
            self.label = label
            self.type = type
            # self.n_authors = len(authors)
            #if self.n_authors > 4:
            #    self.et_al = True
            #    self.authors = authors[:4]
            #else:
            #    self.et_al = False
            #    self.authors = authors
            #    for i in xrange(self.n_authors,4):
            #        self.authors.append('none')
            self.authors = authors
            ''':type : list of dict '''
            self.title = title
            self.date = date


    def create_journal(self):
        self.create_default()

    def create_conference(self):
        self.create_default()

    def create_book(self):
        self.create_default()

    def create_default(self): #todo. doesn't work!!!!
        self.date = int(raw_input('Date: '))
        self.title = raw_input('Title: ')
        self.n_authors = int(raw_input('#authors (only 4 will be introduced):  '))
        self.authors = []

        for i in xrange(self.n_authors):
            self.authors.append(raw_input('    Author {0} full name: '.format(i + 1)))

        if self.n_authors < 4:
            for i in xrange(self.n_authors, 4):
                self.authors.append('none')

        if self.n_authors > 4:
            self.et_al = True
        else:
            self.et_al = False

