import sqlite3

try:
    banco = sqlite3.connect('primeiro_banco.db')
    cursor = banco.cursor()
    #cursor.execute("CREATE TABLE pessoas(nome text, idade integer, email text)")
    #cursor.execute("INSERT INTO pessoas VALUES('Maria', 40, 'maria@gmail.com')")
    #cursor.close()
    cursor.execute("DELETE FROM pessoas WHERE idade = 1.5")
    banco.commit()
    banco.close()
    print('O registro foi removido com sucesso!!!')

except sqlite3.Error as erro:
    print ('Erro ao excluir o registro. Descrição do erro: ', erro)


