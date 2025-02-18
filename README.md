# Z3-Exemples

Este repositório contém diversos exemplos de utilização do [Z3](https://github.com/Z3Prover/z3) em Python. Os exemplos demonstram como trabalhar com **restrições**, **sistemas** de equações, **otimização** e **problemas de satisfatibilidade** (SAT/SMT) utilizando o solver Z3.

## Estrutura do Projeto

- **Complex Exemples**
  - [exemplo2_n_rainhas.py](Complex%20Exemples/exemplo2_n_rainhas.py)  
    *Solução para o problema das N rainhas.*

- **Simple Exemples**
  - **Otimização**
    - [exemplo1.py](Simple%20Exemples/Otimiza%C3%A7%C3%A3o/exemplo1.py)  
      *Minimização de uma função linear simples sujeita a restrições.*
    - [exemplo2.py](Simple%20Exemples/Otimiza%C3%A7%C3%A3o/exemplo2.py)  
      *Otimização lexicográfica com múltiplos objetivos.*
    - [exemplo_final.py](Simple%20Exemples/Otimiza%C3%A7%C3%A3o/exemplo_final.py)  
      *Exemplo de produção industrial multiobjetivo, maximizando lucro e minimizando produção.*
  - **SAT**
    - [exemplo_sat1.py](Simple%20Exemples/SAT/exemplo_sat1.py)  
      *Exemplo de problema SAT com três variáveis booleanas.*
    - [exemplo_sat2.py](Simple%20Exemples/SAT/exemplo_sat2.py)  
      *Exemplo de problema SAT com quatro variáveis booleanas e restrições lógicas.*
  - **SMT**
    - [exemplo_smt1.py](Simple%20Exemples/SMT/exemplo_smt1.py)  
      *Exemplo SMT utilizando aritmética de inteiros.*
    - [exemplo_smt2.py](Simple%20Exemples/SMT/exemplo_smt2.py)  
      *Exemplo SMT com bit-vetores de 8 bits.*

## Instalação

Certifique-se de que a biblioteca Z3 esteja instalada na sua máquina. No terminal, execute:

```sh
pip install z3-solver