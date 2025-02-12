from z3 import *

# Exemplo 4: Otimização com Z3
# Declaramos as variáveis inteiras x e y.
x = Int('x')
y = Int('y')

# Criamos um objeto Optimize para trabalhar com objetivos de otimização.
opt = Optimize()

# Adicionamos as restrições:
#   x + 2*y <= 10, x >= 0 e y >= 0.
opt.add(x + 2*y <= 10, x >= 0, y >= 0)

# Define os objetivos:
#   - Maximizar x.
#   - Minimizar y.
opt.maximize(x)  # Objetivo: maximizar x.
opt.minimize(y)  # Objetivo: minimizar y.

# Executa o processo de otimização.
opt.check()
m = opt.model()
print("Exemplo 4: Solução de otimização:")
print("x =", m[x], ", y =", m[y])
