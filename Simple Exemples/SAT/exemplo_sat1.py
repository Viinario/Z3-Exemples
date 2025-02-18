# exemplo_sat1.py
# Importa todas as funcionalidades do módulo z3
from z3 import *

# Cria um solver para problemas SAT
solver = Solver()

# Declara três variáveis booleanas: A, B e C
A = Bool('A')  # Variável booleana A
B = Bool('B')  # Variável booleana B
C = Bool('C')  # Variável booleana C

# Adiciona as restrições lógicas:
solver.add(Or(A, B))     # Restrição 1: A ou B deve ser verdadeiro
solver.add(Or(Not(A), C))  # Restrição 2: Não A ou C deve ser verdadeiro
solver.add(Or(Not(B), C))  # Restrição 3: Não B ou C deve ser verdadeiro

# Verifica se a fórmula é satisfatível
if solver.check() == sat:
    # Se satisfatível, obtém o modelo (atribuição de valores) que satisfaz as restrições
    model = solver.model()
    # Imprime a solução encontrada
    print("Solução SAT encontrada:")
    print("A =", model[A])
    print("B =", model[B])
    print("C =", model[C])
else:
    print("A fórmula não é satisfatível.")
