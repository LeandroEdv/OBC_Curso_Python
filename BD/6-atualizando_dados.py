import sqlite3
connection = sqlite3.connect('title.db')
cursor = connection.cursor()

id = int(input('Informe o id do filme que deseja atualizar\n'))
name = input('Ingorme o nome do filme\n')

cursor.execute("""
               UPDATE movies set name = ?
               WHERE id = ?
               """,(name, id))

connection.commit()
connection.close()