# Teste_Analytics_IasmimNunes

Repositório desenvolvido como parte do processo seletivo para a vaga de Estagiário de Analytics.

---

## 📌 Objetivo do Projeto

O objetivo deste projeto foi simular um cenário de análise de vendas utilizando Python e SQL, aplicando técnicas de:

- Geração e tratamento de dados
- Limpeza de base
- Análise exploratória
- Criação de métricas de negócio
- Extração de insights para tomada de decisão

---

## 📂 Estrutura do Repositório

- analise-vendas-python.py  
  Script responsável pela simulação, limpeza e análise dos dados.

- data_clean.csv  
  Base de dados tratada e pronta para análise em SQL.

- consultas_sql.sql  
  Arquivo contendo as consultas SQL solicitadas no teste.

- relatorio_insights.pdf  
  Documento com interpretação dos resultados e principais insights.

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Pandas
- NumPy
- Matplotlib
- MySQL
- MySQL Workbench

---

## ⚙️ Dependências

Para executar o script Python, instale as bibliotecas necessárias:

```bash
pip install pandas numpy matplotlib
```

---

## ▶️ Como Executar o Código Python

1. Certifique que o Python está instalado.
2. Instale as dependências listadas acima.
3. Execute o script com o comando:

```bash
python analise-vendas-python.py
```

O script irá:
- Gerar um dataset simulado com mais de 100 registros
- Inserir valores nulos e duplicatas propositalmente
- Realizar a limpeza dos dados
- Criar as colunas Total_Venda e Mes
- Calcular o faturamento mensal
- Identificar o produto mais vendido
- Identificar o mês com maior e menor faturamento
- Gerar um gráfico de tendência mensal
- Exportar o arquivo data_clean.csv

---

## 🗄️ Como Executar as Consultas SQL

1. Importar o arquivo data_clean.csv no MySQL.
2. Criar uma tabela compatível com a estrutura do arquivo.
3. Executar as consultas presentes no arquivo consultas_sql.sql.
4. Analisar os resultados retornados pelo banco de dados.

As consultas realizam:
- Cálculo do total de vendas por produto e categoria.
- Identificação dos produtos com menor desempenho em um mês específico.

---

## Principais Análises Realizadas

- Remoção de registros duplicados.
- Exclusão de valores nulos em colunas essenciais (Quantidade e Preço).
- Cálculo do faturamento total por transação.
- Agrupamento para análise de faturamento mensal.
- Identificação do produto com maior volume de vendas.
- Identificação do mês com maior e menor faturamento.
- Análise de desempenho por produto utilizando SQL.

---

## 📌 Suposições Adotadas

- Os dados foram simulados aleatoriamente para o ano de 2023.
- Foram gerados mais de 100 registros para representar vendas ao longo do ano.
- Valores nulos e duplicatas foram inseridos intencionalmente para simular problemas reais.
- A empresa analisada é fictícia e pertence ao setor de eletrônicos e acessórios.
- Os preços e quantidades foram distribuídos de forma aleatória.

---

## 📈 Conclusão

A integração entre Python e SQL permitiu transformar dados simulados em informações estratégicas. A análise revelou variações no faturamento ao longo do ano, concentração de vendas em determinados produtos e diferenças de desempenho entre períodos.

O processo demonstrou a importância da limpeza e preparação dos dados antes da análise, bem como o uso de consultas estruturadas para extração de insights. O projeto evidencia como técnicas de análise de dados podem apoiar decisões comerciais baseadas em evidências.
