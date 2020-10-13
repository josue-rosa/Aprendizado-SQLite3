import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()
#cursor.execute("CREATE TABLE pessoas(nome text, idade integer, email text)")
#cursor.execute("INSERT INTO pessoas VALUES('Maria', 40, 'maria@gmail.com')")
#cursor.close()

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())
