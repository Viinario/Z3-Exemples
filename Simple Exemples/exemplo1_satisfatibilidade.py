from z3 import *

# Exemplo 1: Problema simples de satisfatibilidade
# Declaramos duas variáveis inteiras: x e y.
x = Int('x')
y = Int('y')

# Criamos o solver.
s = Solver()

# Adicionamos restrições: x deve ser maior que y e y deve ser maior que 5.
s.add(x > y, y > 5)

# Verifica se as restrições são satisfatíveis.
if s.check() == sat:
    print("Exemplo 1: Solução encontrada:")
    print(s.model())  # Exibe um modelo (atribuição) que satisfaz as restrições.
else:
    print("Exemplo 1: Problema sem solução (unsat)")
