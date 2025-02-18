# exemplo_smt1.py
# Importa todas as funcionalidades do módulo z3
from z3 import *

# Cria um solver para problemas SMT usando aritmética de inteiros
solver = Solver()

# Declara duas variáveis inteiras: x e y
x = Int('x')  # Variável inteira x
y = Int('y')  # Variável inteira y

# Adiciona restrições:
solver.add(x > 5)        # Restrição 1: x deve ser maior que 5
solver.add(y == x + 3)     # Restrição 2: y deve ser igual a x mais 3
solver.add(x + y < 20)     # Restrição 3: a soma de x e y deve ser menor que 20

# Verifica se o conjunto de restrições é satisfatível
if solver.check() == sat:
    # Se satisfatível, obtém o modelo com os valores que satisfazem as restrições
    model = solver.model()
    # Imprime a solução encontrada
    print("Solução SMT (aritmética) encontrada:")
    print("x =", model[x])
    print("y =", model[y])
else:
    print("Não foi possível encontrar uma solução satisfatível para as restrições.")
