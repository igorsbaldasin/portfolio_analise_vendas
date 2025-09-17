import random
from datetime import datetime, timedelta

# Listas de dados para geração
produtos_list = [
    ('Smartphone XPTO', 'Eletrônicos', 3500.00),
    ('Notebook Gamer', 'Eletrônicos', 8000.00),
    ('Fone de Ouvido', 'Acessórios', 150.00),
    ('Mouse Sem Fio', 'Acessórios', 80.00),
    ('Monitor Ultrawide', 'Eletrônicos', 1800.00),
    ('Cadeira Gamer', 'Móveis', 1200.00),
    ('Cabo HDMI', 'Acessórios', 30.00),
    ('Webcam HD', 'Eletrônicos', 180.00),
    ('Teclado Mecânico', 'Acessórios', 250.00),
    ('Mochila para Notebook', 'Acessórios', 120.00),
    ('Placa de Vídeo RTX 4080', 'Hardware', 12000.00),
    ('Processador AMD Ryzen 7', 'Hardware', 2500.00)
]
estados_list = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

num_clientes = # quantidade total desejada, no momento existem 147 clientes no banco de dados, ou seja, colocar um valor acima de 147.
num_vendas = # quantidade total desejada, no momento existem 510 vendas no banco de dados, ou seja, colocar um valor acima de 510. 

# --- Gerar Inserts para Produtos ---
print("-- Inserts para a Tabela 'Produtos'")
print("INSERT INTO Produtos (ID_Produto, Nome_Produto, Categoria, Valor_Unitario) VALUES")
for i, (nome, categoria, valor) in enumerate(produtos_list):
    line = f"({i+1}, '{nome}', '{categoria}', {valor:.2f})"
    if i < len(produtos_list) - 1:
        line += ","
    else:
        line += ";"
    print(line)
print("\n")

# --- Gerar Inserts para Clientes ---
print("-- Inserts para a Tabela 'Clientes'")
print("INSERT INTO Clientes (ID_Cliente, CPF_Cliente, Estado) VALUES")
for i in range(148, num_clientes + 1):
    cpf_cnpj = f"'{random.randint(100,999)}.{random.randint(100,999)}.{random.randint(100,999)}-{random.randint(10,99)}'"
    estado = random.choice(estados_list)
    line = f"({i}, {cpf_cnpj}, '{estado}')"
    if i < num_clientes:
        line += ","
    else:
        line += ";"
    print(line)
print("\n")

# --- Gerar Inserts para Vendas ---
print("-- Inserts para a Tabela 'Vendas'")
print("INSERT INTO Vendas (ID_Venda, Data_Venda, ID_Produto, ID_Cliente, Quantidade) VALUES")
start_date = datetime(2025, 1, 1)
for i in range(511, num_vendas + 1):
    data_venda = start_date + timedelta(days=random.randint(0, 200))
    id_produto = random.randint(1, len(produtos_list))
    id_cliente = random.randint(1, num_clientes)
    quantidade = random.randint(1, 5)
    
    line = f"({i}, '{data_venda.strftime('%Y-%m-%d')}', {id_produto}, {id_cliente}, {quantidade})"
    if i < num_vendas:
        line += ","
    else:
        line += ";"
    print(line)