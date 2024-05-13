import sqlite3
connection = sqlite3.connect('title.db')
cursor = connection.cursor()

data = cursor.execute('''
                      SELECT * FROM movies
                      ''')
print(data.fetchall())

for row in cursor.execute('SELECT * FROM movies'):
    print(f'{row}')
    
for row in cursor.execute('SELECT * FROM movies ORDER BY score desc'):
    print(f'{row}')    
    
connection.close()