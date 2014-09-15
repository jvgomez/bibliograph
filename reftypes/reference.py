class Reference:

    def __init__(self):
        ref_types = { 1 : self.create_journal,
                      2 : self.create_conference,
                      3 : self.create_book,
                      4 : self.create_default
                    }

        self.ref_type = int(raw_input('Type of article (1 journal, 2 conf, 3 book, 4 other): '))
        ref_types[self.ref_type]()

    def create_journal(self):
        self.create_default()

    def create_conference(self):
        self.create_default()

    def create_book(self):
        self.create_default()

    def create_default(self):
        self.year = int(raw_input('Year: '))
        self.title = raw_input('Title: ')
        self.n_authors = int( raw_input('#authors (only 4 will be introduced):  '))
        self.authors = []

        for i in xrange(self.n_authors):
            self.authors.append(raw_input('    Author {0} full name: '.format(i+1)))

        if self.n_authors < 4:
            for i in xrange(self.n_authors,4):
                self.authors.append('none')


        if self.n_authors > 4:
            self.et_al = True
        else:
            self.et_al = False
