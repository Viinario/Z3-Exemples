#Objetivo: Demonstração do poder do Z3 Optimize com um problema de produção industrial multiobjetivo.
#Neste cenário, uma fábrica produz dois produtos (Produto A e Produto B) usando recursos limitados (horas de máquina e mão de obra). O problema possui dois objetivos:
#Objetivo primário: Maximizar o lucro total.
#Objetivo secundário: Minimizar a produção total (para evitar superprodução desnecessária).
# exemplo_final.py
# Importa todas as funcionalidades do módulo z3
from z3 import *

# Cria um objeto de otimização para o problema
otimizador = Optimize()

# Declara variáveis inteiras para as quantidades produzidas de cada produto
produtoA = Int('produtoA')  # Quantidade a produzir do Produto A
produtoB = Int('produtoB')  # Quantidade a produzir do Produto B

# Adiciona restrições referentes à disponibilidade de recursos:
# Restrição de horas de máquina:
# Cada unidade de Produto A consome 3 horas e cada unidade de Produto B consome 2 horas.
# A fábrica possui um total de 100 horas de máquina disponíveis.
otimizador.add(3 * produtoA + 2 * produtoB <= 100)

# Restrição de mão de obra:
# Cada unidade de Produto A consome 2 horas de trabalho e cada unidade de Produto B consome 4 horas.
# Há um total de 80 horas de mão de obra disponíveis.
otimizador.add(2 * produtoA + 4 * produtoB <= 80)

# Restrições de não negatividade: não é possível produzir quantidades negativas
otimizador.add(produtoA >= 0)
otimizador.add(produtoB >= 0)

# Define os lucros gerados por cada produto:
# Produto A gera um lucro de 50 por unidade e Produto B gera um lucro de 40 por unidade.
lucro_total = 50 * produtoA + 40 * produtoB

# Define o objetivo primário: maximizar o lucro total
otimizador.maximize(lucro_total)

# Define o objetivo secundário: minimizar a produção total (produtoA + produtoB)
# Isso pode representar uma estratégia para evitar produzir mais do que o necessário.
producao_total = produtoA + produtoB
otimizador.minimize(producao_total)

# Executa a verificação para encontrar uma solução que satisfaça as restrições e otimize os objetivos
otimizador.check()

# Obtém o modelo (solução ótima) encontrado pelo otimizador
modelo = otimizador.model()

# Imprime a solução ótima encontrada, mostrando as quantidades a produzir e os valores dos objetivos
print("Solução ótima para a produção:")
print("Quantidade de Produto A =", modelo[produtoA])
print("Quantidade de Produto B =", modelo[produtoB])
print("Lucro Total =", modelo.evaluate(lucro_total))
print("Produção Total =", modelo.evaluate(producao_total))
