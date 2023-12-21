import sqlite3

conn = sqlite3.connect('database.db')

# Table Utilisateur 
conn.execute('''CREATE TABLE Utilisateurs
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nom TEXT NOT NULL,
             prenom TEXT NOT NULL,
             email TEXT NOT NULL UNIQUE,
             motdepasse TEXT NOT NULL)''')

# Table Role
conn.execute('''CREATE TABLE Role
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             description TEXT NOT NULL)''')

# Table Commentaire 
conn.execute('''CREATE TABLE Commentaire 
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             commentaire TEXT NOT NULL,
             article_id INTEGER NOT NULL,
             utilisateur_id INTEGER NOT NULL,
             FOREIGN KEY(article_id) REFERENCES Article(id),
             FOREIGN KEY(utilisateur_id) REFERENCES Utilisateurs(id))''')


# Table Article
conn.execute('''CREATE TABLE Article
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            contenu TEXT NOT NULL,
            date_publication INTEGER NOT NULL,
            utilisateur_id INTEGER NOT NULL,
            FOREIGN KEY (utilisateur_id) REFERENCES Utilisateurs (id))''')

# Table MotsCles
conn.execute('''CREATE TABLE MotsCles (
            article_id INTEGER NOT NULL,
            motcle_id INTEGER NOT NULL,
            PRIMARY KEY (article_id, motcle_id),
            FOREIGN KEY (article_id) REFERENCES Article (id),
            FOREIGN KEY (motcle_id) REFERENCES MotsCles (id)''')

conn.close()



