import sqlite3
connection = sqlite3.connect('title.db')
cursor = connection.cursor()

id = int(input('Informe o id do filme que deseja Remover\n'))

cursor.execute("""
               DELETE FROM movies
               WHERE id = ?
               """,(id,))

connection.commit()
connection.close()