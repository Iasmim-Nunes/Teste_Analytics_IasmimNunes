import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Simulando dataset
np.random.seed(42)
num_registros = 100  # Mais de 50 registros
datas = pd.date_range(start="2023-01-01", end="2023-12-31", periods=num_registros)
produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Impressora"]
categorias = ["Eletrônicos", "Acessórios"]

dados = {
    "ID": range(1, num_registros + 1),
    "Data": np.random.choice(datas, num_registros),
    "Produto": np.random.choice(produtos, num_registros),
    "Categoria": np.random.choice(categorias, num_registros),
    "Quantidade": np.random.randint(1, 10, num_registros),
    "Preco": np.random.uniform(50, 5000, num_registros).round(2)
}

df = pd.DataFrame(dados)

# Inserindo propositalmente valores nulos para simular problema real
df.loc[5, "Quantidade"] = None
df.loc[10, "Preco"] = None

# Inserindo duplicata
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

print("Dataset inicial criado com sucesso!")
print(df.head())

#  Limpeza de dados
# Converter Data para datetime
df["Data"] = pd.to_datetime(df["Data"])

# Verificar valores nulos
print("\nValores nulos antes da limpeza:")
print(df.isnull().sum())

# Remover duplicatas
df = df.drop_duplicates()

# Remove linhas com nulos em colunas essenciais
df = df.dropna(subset=["Quantidade", "Preco"])

print("\nValores nulos após limpeza:")
print(df.isnull().sum())

# Cria a coluna Total_Venda
df["Total_Venda"] = df["Quantidade"] * df["Preco"]

# Cria a coluna Mes
df["Mes"] = df["Data"].dt.month

# Faturamento mensal
faturamento_mensal = df.groupby("Mes")["Total_Venda"].sum().sort_index()

print("\nFaturamento mensal:")
print(faturamento_mensal)

# Produto mais vendido
produto_mais_vendido = df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

print("\nProduto mais vendido:")
print(produto_mais_vendido)

# INSIGHTS REAIS
print("\nINSIGHTS:")
print(f"- O produto mais vendido foi {produto_mais_vendido.idxmax()} com {produto_mais_vendido.max()} unidades vendidas.")
print(f"- O mês com maior faturamento foi {faturamento_mensal.idxmax()}.")
print(f"- O mês com menor faturamento foi {faturamento_mensal.idxmin()}.")

# Visualização do faturamento mensal
plt.figure()
plt.plot(faturamento_mensal.index, faturamento_mensal.values)
plt.xlabel("Mês")
plt.ylabel("Faturamento Total")
plt.title("Tendência de Vendas Mensais - 2023")
plt.grid(True)
plt.show()

# Salvando arquivo limpo
print("Arquivo será salvo em:", os.getcwd())
df.to_csv("data_clean.csv", sep=";", index=False, encoding="utf-8-sig")
print("\nArquivo data_clean.csv salvo com sucesso!")
