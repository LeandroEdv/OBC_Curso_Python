import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect("title.db")

# 2 - Criando um cursor
'''
Cursor é um interador que permite
navegar e manipular os do bd.
'''
cursor = connection.cursor()

name = input('Nime do filme\n')
year = int(input('Ano do filme\n'))
score = float(input('Nota do filme\n'))

cursor.execute("""
               INSERT INTO movies(name, year, score)
               VALUES(?, ?, ?)
               """, (name, year, score))

connection.commit()
connection.close()