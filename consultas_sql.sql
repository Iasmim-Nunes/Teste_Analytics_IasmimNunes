CREATE DATABASE analise_vendas;
USE analise_vendas;

CREATE TABLE Vendas (
    ID INT,
    Data DATE,
    Produto VARCHAR(100),
    Categoria VARCHAR(100),
    Quantidade INT,
    Preco DECIMAL(10,2),
    Total_Venda DECIMAL(12,2),
    Mes INT
);

SELECT 
    Produto,
    Categoria,
    SUM(Quantidade * Preco) AS Total_Vendas
FROM Vendas
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;

SELECT Produto, SUM(Quantidade) AS Total_Vendido
FROM Vendas
WHERE Mes = 6
GROUP BY Produto
ORDER BY Total_Vendido ASC
LIMIT 1;