import sqlite3

nome = "Davi"
idade = 3.5
email = "davi@gmail.com"

try:
    banco = sqlite3.connect('primeiro_banco.db')
    cursor = banco.cursor()
    #cursor.execute("CREATE TABLE pessoas(nome text, idade integer, email text)")
    cursor.execute("INSERT INTO pessoas VALUES('"+nome+"', "+str(idade)+", '"+email+"')")
    banco.commit()
    cursor.close()
    print("Registro inserido com sucesso")

except sqlite3.Error as erro:
    print('Problema ao inserir o registro', erro)
