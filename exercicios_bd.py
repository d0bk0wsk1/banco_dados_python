#1. Crie uma tabela chamada "alunos" com os seguintes campos: id
#(inteiro), nome (texto), idade (inteiro) e curso (texto).

import sqlite3

conexao = sqlite3.connect('banco_dados')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE alunos (id INT,nome VARCHAR(100), idade INT , curso VARCHAR(100))')


#2. Insira pelo menos 5 registros de alunos na tabela que você criou no #exercício anterior.
cursor.execute('INSERT INTO alunos (id,nome, idade, curso) VALUES (1, "Paula", 21, "Química")')
cursor.execute('INSERT INTO alunos (id,nome, idade, curso) VALUES (2, "Guilherme", 23, "ADS")')
cursor.execute('INSERT INTO alunos (id,nome, idade, curso) VALUES (3, "Gabriela", 27, "Fisioterapia")')
cursor.execute('INSERT INTO alunos (id,nome, idade, curso) VALUES (4, "Barbara", 23, "Medicina")')
cursor.execute('INSERT INTO alunos (id,nome, idade, curso) VALUES (5, "Arthur", 20, "Química")')

#3. Consultas Básicas Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
cursor.execute('SELECT * FROM alunos')

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
cursor.execute('SELECT nome, idade FROM alunos WHERE curso = "Engenharia" ORDER BY nome ASC')

#d) Contar o número total de alunos na tabela
cursor.execute('SELECT COUNT(id) FROM alunos GROUP BY id')

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade = 21 WHERE id = 2')
#b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos WHERE id = 3')


#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave
#primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
#registros de clientes na tabela.
cursor.execute('CREATE TABLE clientes (id INT,nome VARCHAR(100), idade INT , saldo FLOAT)')
cursor.execute('INSERT INTO clientes (id,nome, idade, saldo) VALUES (1, "Paula", 32, 12.34)')
cursor.execute('INSERT INTO clientes (id,nome, idade, saldo) VALUES (2, "Guilherme", 33, 234.45)')
cursor.execute('INSERT INTO clientes (id,nome, idade, saldo) VALUES (3, "Gabriela", 37, 356.23)')
cursor.execute('INSERT INTO clientes (id,nome, idade, saldo) VALUES (4, "Barbara", 23, 763.23)')
cursor.execute('INSERT INTO clientes (id,nome, idade, saldo) VALUES (5, "Arthur", 30, 123.34)')


#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

#b) Calcule o saldo médio dos clientes.
cursor.execute('SELECT AVG(saldo) FROM clientes')

#c) Encontre o cliente com o saldo máximo.
cursor.execute('SELECT nome, saldo FROM clientes ORDER BY saldo DESC LIMIT 1')

#d) Conte quantos clientes têm saldo acima de 1000.
cursor.execute('SELECT COUNT(id) FROM clientes WHERE saldo > 1000 GROUP BY id')

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo = 2134.23 WHERE id = 2')
#b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE id = 2')

#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id
#(chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas
#compras associadas a clientes existentes na tabela "clientes".
cursor.execute('''CREATE TABLE compras (
                    id INTEGER PRIMARY KEY,
                    cliente_id INTEGER,
                    produto TEXT,
                    valor REAL,
                    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
                )''')
cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (1, "Biscoito", 2.30)')
cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (2, "Roupa", 130.45)')
cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (3, "Remedio", 345.34)')

#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
dados = cursor.execute('''SELECT c.nome, co.produto, co.valor
                  FROM clientes AS c
                  JOIN compras AS co ON c.id = co.cliente_id''')
for row in dados:
    print("Nome do Cliente:", row[0])
    print("Produto:", row[1])
    print("Valor:", row[2])
    print()