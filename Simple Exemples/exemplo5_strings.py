from z3 import *

# Exemplo 5: Resolvendo restrições com strings
# Declaramos uma variável string.
str_var = String('str_var')

# Criamos o solver.
s = Solver()

# Adicionamos as restrições:
# - Length(str_var) > 10: o comprimento da string deve ser maior que 10.
# - StartsWith(str_var, StringVal("Hello")): a string deve começar com "Hello".
s.add(Length(str_var) > 10, PrefixOf(StringVal("Hello"), str_var))

# Verifica se há uma string que satisfaça as restrições.
if s.check() == sat:
    m = s.model()
    print("Exemplo 5: Solução para a string:")
    print(m[str_var])
else:
    print("Exemplo 5: Sem solução para as restrições da string.")
