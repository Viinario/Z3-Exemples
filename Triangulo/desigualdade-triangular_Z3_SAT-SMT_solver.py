from z3 import Solver, Int, And, Not, Or, sat

# Criando as variáveis para os lados do triângulo
a = Int('a')
b = Int('b')
c = Int('c')

# Função para bloquear soluções repetidas
def bloquear_solucao(solver, solucao, variaveis):
    restricoes = []
    for v in variaveis:
        restricoes.append(v != solucao[v])
    solver.add(Or(restricoes))

# ========= PASSO 1: Verificando se podemos formar um triângulo =========
solver1 = Solver()

# Restrições básicas: todos os lados devem ser positivos
solver1.add(a > 0)
solver1.add(b > 0)
solver1.add(c > 0)

# Adicionando a condição da desigualdade triangular
solver1.add(a + b > c)
solver1.add(a + c > b)
solver1.add(b + c > a)

# Executando a verificação
print("Passo 1: Verificando se podemos formar um triângulo:")
resultado1 = solver1.check()
print(resultado1)

# Listando os primeiros 10 exemplos válidos
contador = 0
while resultado1 == sat and contador < 10:
    modelo = solver1.model()
    print(modelo)
    bloquear_solucao(solver1, modelo, [a, b, c])
    resultado1 = solver1.check()
    contador += 1

# ========= PASSO 2: "Negando a condição" =========
solver2 = Solver()

# Restrições básicas: todos os lados devem ser positivos
solver2.add(a > 0)
solver2.add(b > 0)
solver2.add(c > 0)

# Adicionando a negação parcial da condição de triângulo
solver2.add(Not(And(a + b > c, a + c > b, b + c > a)))

# Executando a verificação
print("\nPasso 2: Negando a condição e verificando se ainda é possível formar um triângulo:")
resultado2 = solver2.check()
print(resultado2)

# Listando os primeiros 10 exemplos válidos
contador = 0
while resultado2 == sat and contador < 10:
    modelo = solver2.model()
    print(modelo)
    bloquear_solucao(solver2, modelo, [a, b, c])
    resultado2 = solver2.check()
    contador += 1

# ========= PASSO 3: Negando completamente a condição =========
solver3 = Solver()

# Restrições básicas: todos os lados devem ser positivos
solver3.add(a > 0)
solver3.add(b > 0)
solver3.add(c > 0)

# Adicionando a negação total da condição de triângulo
solver3.add(And(Not(a + b > c), Not(a + c > b), Not(b + c > a)))

# Executando a verificação
print("\nPasso 3: Negando totalmente a condição e verificando se ainda é possível formar um triângulo:")
resultado3 = solver3.check()
print(resultado3)  # Deve imprimir UNSAT

# Listando os primeiros 10 exemplos válidos
contador = 0
while resultado3 == sat and contador < 10:
    modelo = solver3.model()
    print(modelo)
    bloquear_solucao(solver3, modelo, [a, b, c])
    resultado3 = solver3.check()
    contador += 1