from z3 import *

# Exemplo 2: Problema das N Rainhas
# Função que resolve o problema das N rainhas.
def solve_n_queens(n):
    # Cada rainha é representada por uma variável que indica a coluna
    # em que ela está posicionada na linha correspondente.
    queens = [Int(f'q_{i}') for i in range(n)]
    s = Solver()
    
    # Cada rainha deve estar posicionada em uma coluna entre 0 e n-1.
    for q in queens:
        s.add(q >= 0, q < n)
    
    # Não pode haver duas rainhas na mesma coluna.
    s.add(Distinct(queens))
    
    # Restrições para que rainhas não se ataquem na diagonal.
    # Duas rainhas nas posições (i, queens[i]) e (j, queens[j])
    # não podem estar na mesma diagonal se |queens[i] - queens[j]| == |i - j|.
    for i in range(n):
        for j in range(i + 1, n):
            s.add(Abs(queens[i] - queens[j]) != j - i)
    
    # Verifica se há solução e, se houver, retorna as posições.
    if s.check() == sat:
        m = s.model()
        return [m.evaluate(queens[i]) for i in range(n)]
    else:
        return None

# Resolve o problema para 8 rainhas.
solution = solve_n_queens(8)
if solution:
    print("Exemplo 2: Solução para o problema das 8 rainhas:")
    print(solution)
else:
    print("Exemplo 2: Sem solução para o problema das 8 rainhas.")
