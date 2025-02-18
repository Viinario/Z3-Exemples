from z3 import Solver, Ints, And, Not, sat, unsat

# Criando as variáveis para os lados do triângulo
a, b, c = Ints('a b c')

# Criamos o solver
s = Solver()

# Os lados devem ser positivos
s.add(a > 0, b > 0, c > 0)

# PASSO 1: Condição normal
s.push()  # Salva o estado do solver
s.add(And(a + b > c, a + c > b, b + c > a))  # Desigualdade triangular

# PASSO 2: Negação parcial
# s.push()
# s.add(Not(And(a + b > c, a + c > b, b + c > a)))  # Negamos parcialmente

# PASSO 3: Negação completa
# s.push()
# s.add(And(Not(a + b > c), Not(a + c > b),Not( b + c > a)))  # Negamos toda a condição

print(s.check())
if s.check() == sat:
    print(s.model())
