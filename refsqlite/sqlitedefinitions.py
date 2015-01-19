CREATE_AUTHORS_TABLE = '''CREATE TABLE "Authors" (
    "Name" TEXT NOT NULL,
    "Middle" TEXT,
    "Lastname" TEXT NOT NULL,
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
);'''

CREATE_ARTICLES_TABLE = '''CREATE TABLE "Articles" (
    "Title" TEXT NOT NULL,
    "Date" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "Label" TEXT,
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
);'''

CREATE_AIA_TABLE = '''CREATE TABLE "main"."AuthorsInArticles" (
    "Article" INTEGER NOT NULL,
    "Author" INTEGER NOT NULL,
     FOREIGN KEY(Article) REFERENCES Articles(ID),
     FOREIGN KEY(Author) REFERENCES Authors(ID)
);'''

CREATE_REFERENCES_TABLE = '''CREATE TABLE "References" (
    "Article" INTEGER NOT NULL,
    "Reference" INTEGER NOT NULL,
    FOREIGN KEY(Article) REFERENCES Articles(ID),
    FOREIGN KEY(Reference) REFERENCES Articles(ID)
);'''

AIA_VIEW = '''SELECT  ar.title,
    case  when au.middle is null then
      au.name || ' ' || au.lastName
    when au.middle is not null then
        au.name || ' ' || au.middle || ' ' ||au.lastName
    end as [full name]
       FROM authorsinarticles as aia
    JOIN authors as au ON au.ID = aia.author
    JOIN articles as ar ON ar.ID = aia.article
'''
