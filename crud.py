import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='primeirocrud',
)

cursor = conexao.cursor()

###############################   CREATE   ###############################

# nomeProduto = "Milka Chocolate"
# valorProduto = 11

# comando = f'INSERT INTO vendas (nomeProduto, valorProduto) VALUES ("{nomeProduto}", {valorProduto})'
# cursor.execute(comando)

# Edita o Banco de Dados
# conexao.commit() 

###############################   READ   ###############################

# comando = f'SELECT * FROM vendas'

# cursor.execute(comando)

# Ler o Banco de Dados
# resultado = cursor.fetchall()
# print(resultado)

###############################   UPDATE   ###############################

# nomeProduto = "Milka Chocolate"
# valorProduto = 11

# comando = f'UPDATE vendas SET valorProduto = {valorProduto} WHERE nomeProduto = "{nomeProduto}"'
# cursor.execute(comando)

# Edita o Banco de Dados
# conexao.commit()

###############################   DELETE   ###############################

# nomeProduto = "Milka Chocolate"
# valor = 11

# comando = f'DELETE FROM vendas WHERE nomeProduto = "{nomeProduto}"'
# cursor.execute(comando)

#Edita o Banco de Dados
# conexao.commit()



cursor.close()
conexao.close()



