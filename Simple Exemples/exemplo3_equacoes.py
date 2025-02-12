from z3 import *

# Exemplo 3: Resolvendo um sistema de equações
# Declaramos duas variáveis inteiras: x e y.
x, y = Ints('x y')

# Criamos o solver e adicionamos as restrições:
# 1. x^2 + y^2 = 25
# 2. x > y
# 3. x > 0 e y > 0 (só procuramos soluções positivas)
s = Solver()
s.add(x**2 + y**2 == 25, x > y, x > 0, y > 0)

# Verifica se o sistema é satisfatível e exibe a solução encontrada.
if s.check() == sat:
    m = s.model()
    print("Exemplo 3: Solução do sistema:")
    print("x =", m[x], ", y =", m[y])
else:
    print("Exemplo 3: Sem solução para o sistema.")
