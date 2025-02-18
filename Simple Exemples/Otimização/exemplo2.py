# Objetivo: Otimização com múltiplos objetivos (lexicográfico). Neste exemplo, maximizamos duas variáveis sujeitas a uma restrição.
# exemplo2.py
# Importa todas as funcionalidades do módulo z3
from z3 import *

# Cria um objeto de otimização
otimizador = Optimize()

# Declara duas variáveis inteiras, a e b, que serão otimizadas
a = Int('a')  # Variável inteira a
b = Int('b')  # Variável inteira b

# Adiciona restrições ao problema:
otimizador.add(a + b <= 20)  # Garante que a soma de a e b seja no máximo 20
otimizador.add(a >= 0)       # Garante que a seja não-negativa
otimizador.add(b >= 0)       # Garante que b seja não-negativa

# Define dois objetivos a serem otimizados:
# Primeiro, maximiza o valor de a
h1 = otimizador.maximize(a)
# Em seguida, maximiza o valor de b (dentro dos limites impostos pela otimização anterior)
h2 = otimizador.maximize(b)

# Executa a verificação para encontrar uma solução que satisfaça as restrições e otimize os objetivos
otimizador.check()

# Obtém o modelo (solução) resultante
modelo = otimizador.model()

# Imprime a solução encontrada, mostrando os valores de a e b
print("Solução encontrada:")
print("a =", modelo[a])
print("b =", modelo[b])
