# Objetivo: Minimizar uma função linear simples sujeita a restrições.
# exemplo1.py
# Importa todas as funcionalidades do módulo z3
from z3 import *

# Cria um objeto de otimização, que permitirá adicionar restrições e definir a função objetivo
otimizador = Optimize()

# Declara duas variáveis inteiras, x e y, que serão usadas no problema
x = Int('x')  # Variável inteira x
y = Int('y')  # Variável inteira y

# Adiciona restrições ao problema:
otimizador.add(x + y >= 10)  # Garante que a soma de x e y seja no mínimo 10
otimizador.add(x >= 0)       # Garante que x seja não-negativo
otimizador.add(y >= 0)       # Garante que y seja não-negativo

# Define a função objetivo a ser minimizada: f(x, y) = x + 2*y
objetivo = x + 2 * y
otimizador.minimize(objetivo)  # Informa ao otimizador que queremos minimizar a função objetivo

# Executa a verificação para encontrar uma solução que satisfaça as restrições e otimize o objetivo
otimizador.check()

# Obtém o modelo (solução) encontrado pelo otimizador
modelo = otimizador.model()

# Imprime a solução encontrada, mostrando os valores de x, y e o valor mínimo da função objetivo
print("Solução encontrada:")
print("x =", modelo[x])
print("y =", modelo[y])
print("Valor mínimo de x + 2*y =", modelo.evaluate(objetivo))
