# exemplo_smt2.py
# Importa todas as funcionalidades do módulo z3
from z3 import *

# Cria um solver para problemas SMT com bit-vetores
solver = Solver()

# Declara duas variáveis bit-vetor de 8 bits: a e b
a = BitVec('a', 8)  # Variável bit-vetor de 8 bits para a
b = BitVec('b', 8)  # Variável bit-vetor de 8 bits para b

# Adiciona restrições:
solver.add(a > 10)       # Restrição 1: a deve ser maior que 10
solver.add(b < 50)       # Restrição 2: b deve ser menor que 50
solver.add(a + b == 100)   # Restrição 3: a soma de a e b deve ser igual a 100

# Verifica se as restrições são satisfatíveis
if solver.check() == sat:
    # Se satisfatível, obtém o modelo com os valores para a e b
    model = solver.model()
    # Imprime a solução encontrada
    print("Solução SMT (bit-vetor) encontrada:")
    print("a =", model[a])
    print("b =", model[b])
else:
    print("Não foi possível encontrar uma solução satisfatível para as restrições.")