from z3 import *

# =============================================
# Parte 1: Enumeração de todas as soluções
# que atingem o lucro máximo
# =============================================

# Neste exemplo, usamos os produtos X e Y com a seguinte restrição:
# 6*x + 5*y <= 190, e o lucro é dado por 60*x + 50*y.
# Como 60*x + 50*y = 10*(6*x + 5*y), para maximizar o lucro
# a restrição se torna 6*x + 5*y == 190.
# Além disso, x e y são inteiros não-negativos.

# Cria um solver para enumerar as soluções
s = Solver()
x = Int('x')
y = Int('y')

# Adiciona as restrições: máximo lucro (saturando a restrição) e não negatividade
s.add(6 * x + 5 * y == 190, x >= 0, y >= 0)

# Lista para armazenar todas as soluções encontradas
solucoes = []

# Loop para enumerar todas as soluções que satisfazem as restrições
while s.check() == sat:
    modelo = s.model()
    sol = (modelo[x].as_long(), modelo[y].as_long())
    solucoes.append(sol)
    # Adiciona uma cláusula de bloqueio para não repetir essa solução
    s.add(Or(x != modelo[x], y != modelo[y]))

print("Todas as soluções que atingem o lucro máximo:")
for sol in solucoes:
    prod_total = sol[0] + sol[1]
    print("Produto X =", sol[0], "Produto Y =", sol[1], "=> Produção Total =", prod_total)

# =============================================
# Parte 2: Otimização para minimizar a produção total
# dentre as soluções que atingem o lucro máximo
# =============================================

# Cria um otimizador (Optimize) com as mesmas restrições
opt = Optimize()
# Reutilizamos as variáveis x e y (note que são novas instâncias para o otimizador)
x_opt = Int('x_opt')
y_opt = Int('y_opt')

# As restrições de máximo lucro e não negatividade:
opt.add(6 * x_opt + 5 * y_opt == 190, x_opt >= 0, y_opt >= 0)

# Define a produção total e minimiza esse critério
producao_total = x_opt + y_opt
h = opt.minimize(producao_total)

# Executa a otimização
opt.check()
modelo_opt = opt.model()

print("\nSolução escolhida pelo minimize:")
print("Produto X =", modelo_opt[x_opt], 
      "Produto Y =", modelo_opt[y_opt], 
      "=> Produção Total =", modelo_opt.evaluate(producao_total))
