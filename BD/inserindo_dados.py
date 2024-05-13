import sqlite3

connection = sqlite3.connect('title.db')

cursor = connection.cursor()

cursor.execute('''
               INSERT INTO movies (name, year,score)
               VALUES ("SUPER MARIO", "2023", "10")
               ''')
connection.commit()
print('Dados inseridos com sucesso')
connection.close()