# portfolio_analise_vendas
Projeto de Análise de Dados de ponta a ponta. Demonstrando um pipeline completo de SQL (modelagem) e Python (geração de dados) até a criação de um dashboard estratégico no Power BI. O foco é transformar dados brutos em insights de negócio.

Análise de Dados de Vendas de Varejo
Resumo do Projeto
Este projeto demonstra um pipeline completo de Análise de Dados, transformando um conjunto de dados brutos de vendas em um dashboard interativo e insights de negócio claros. O objetivo foi construir uma solução que permite a um gerente de vendas monitorar o desempenho e tomar decisões estratégicas com base em dados.

Tecnologias e Ferramentas
Modelagem de Dados & ETL: SQL Server
Geração de Dados: Python
Visualização & Business Intelligence: Power BI
Controle de Versão: Git & GitHub

O Processo de Análise
1. Modelagem e Preparação dos Dados
Primeiramente, foi projetado um banco de dados relacional com o objetivo de garantir a integridade e a escalabilidade dos dados. O modelo de dados é composto por:

Tabelas de Dimensão: Categorias, Produtos e Clientes.

Tabela de Fatos: Vendas.

Para facilitar a análise e a visualização, foi criada uma VIEW no SQL (Pedido_completo) que consolida os dados de todas as tabelas em uma única visão lógica.

2. Geração de Dados:
Utilizando um script em Python, um conjunto de mais de 200 registros de vendas e dezenas de clientes e produtos foi gerado de forma aleatória, simulando um ambiente de dados real. Isso permitiu a criação de um volume de dados robusto para a análise.

3. Visualização e Dashboard:
A View Pedido_completo foi importada para o Power BI, onde os dados foram transformados em um dashboard profissional. O painel foi projetado para ser intuitivo e responder a perguntas de negócio, como:

Qual o faturamento total e o número de transações?

Quais produtos e categorias são os mais rentáveis?

Como as vendas evoluíram ao longo do tempo?

Principais Análises e Conclusões
Faturamento Total: O dashboard revela um faturamento total de R$ 4,01 MI no período analisado.

Top 3 Produtos: Os produtos que mais contribuíram para o faturamento foram Placa de vídeo RTX 4080, Notebook Gamer e Smartphone XPTO.

Performance por Categoria: A categoria de Eletrônicos foi a mais lucrativa, representando aproximadamente 51,6% do faturamento total.

Tendência de Vendas: A análise mensal mostra que houveram picos de vendas em janeiro e maio, com destaque para maio, que atingiu um total de R$ 389.740,00 de faturamento, sendo o mês que mais gerou receitas. A análise também mostra que houve uma queda abrupta em julho, com apenas R$ 200.600,00, sendo o mês com menor faturamento. Com esses dados, é possível verificar que houve uma variação de R$ 189.140,00, entre os meses com maior e menor faturamento.

Visualização do Dashboard

Abaixo, a visualização do dashboard final, que resume todas as análises:
![Imagem do WhatsApp de 2025-09-16 à(s) 20 40 45_de9314ea](https://github.com/user-attachments/assets/2be3718d-c454-442f-9210-16a3c2057630)
