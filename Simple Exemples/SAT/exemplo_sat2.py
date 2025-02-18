# exemplo_sat2.py
# Importa todas as funcionalidades do módulo z3
from z3 import *

# Cria um solver para problemas SAT
solver = Solver()

# Declara quatro variáveis booleanas: p, q, r e s
p = Bool('p')  # Variável booleana p
q = Bool('q')  # Variável booleana q
r = Bool('r')  # Variável booleana r
s = Bool('s')  # Variável booleana s

# Adiciona restrições lógicas:
solver.add(Or(p, q))         # Restrição 1: p ou q deve ser verdadeiro
solver.add(Or(Not(p), r))      # Restrição 2: Se p é verdadeiro, então r deve ser verdadeiro
solver.add(Or(Not(q), s))      # Restrição 3: Se q é verdadeiro, então s deve ser verdadeiro
solver.add(Or(Not(r), Not(s))) # Restrição 4: Não podem ser ambos r e s verdadeiros simultaneamente

# Verifica se a fórmula é satisfatível
if solver.check() == sat:
    # Se satisfatível, obtém o modelo (atribuição de valores)
    model = solver.model()
    # Imprime a solução encontrada
    print("Solução SAT encontrada:")
    print("p =", model[p])
    print("q =", model[q])
    print("r =", model[r])
    print("s =", model[s])
else:
    print("A fórmula não é satisfatível.")
