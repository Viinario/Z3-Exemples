from z3 import Solver, Ints, Or, And, Not, sat

x, y, z = Ints('x y z')
s = Solver()

s.add(x >= 0, x <= 9)
s.add(y >= 0, y <= 9)
s.add(z >= 0, z <= 9)

# 6 3 7 -> nada está correto
s.add(x != 6, x != 3, x != 7)
s.add(y != 6, y != 3, y != 7)
s.add(z != 6, z != 3, z != 7)
#
# # 6 7 4 -> um numero correto mas no lugar errado
# s.add(
#     Or(
#         And(x == 7, Not(y == 6), Not(z == 6), Not(y == 4), Not(z == 4)),
#         And(x == 4, Not(y == 6), Not(z == 6), Not(y == 7), Not(z == 7)),
#
#         And(y == 6, Not(x == 7), Not(z == 7), Not(x == 4), Not(z == 4)),
#         And(y == 4, Not(x == 6), Not(z == 6), Not(x == 7), Not(z == 7)),
#
#         And(z == 6, Not(x == 7), Not(y == 7), Not(x == 4), Not(y == 4)),
#         And(z == 7, Not(x == 6), Not(y == 6), Not(x == 4), Not(y == 4)),
#     )
# )
# 2 7 8 -> um numero correto no lugar correto
s.add(
    Or(
        And(x == 2, Not(y == 7), Not(z == 8)),
        And(Not(x == 2), y == 7, Not(z == 8)),
        And(Not(x == 2), Not(y == 7), z == 8),
    )
)
#
# # 8 4 2 -> dois numeros corretos, mas no lugar errado
s.add(
    Or(
        And(x == 4, y == 2, Not(z == 8)),
        And(x == 2, y == 8, Not(z == 4)),

        And(x == 4, z == 8, Not(y == 2)),
        And(x == 2, z == 4, Not(y == 8)),

        And(y == 8, z == 4, Not(x == 2)),
        And(y == 2, z == 8, Not(x == 4)),
    )
)
#
# # 2 1 5 -> um numero correto mas no lugar errado
# s.add(
#     Or(
#         And(x == 1, Not(y == 2), Not(z == 2), Not(y == 5), Not(z == 5)),
#         And(x == 5, Not(y == 2), Not(z == 2), Not(y == 1), Not(z == 1)),
#
#         And(y == 2, Not(x == 1), Not(z == 1), Not(x == 5), Not(z == 5)),
#         And(y == 5, Not(x == 2), Not(z == 2), Not(x == 1), Not(z == 1)),
#
#         And(z == 2, Not(x == 1), Not(y == 1), Not(x == 5), Not(y == 5)),
#         And(z == 1, Not(x == 2), Not(y == 2), Not(x == 5), Not(y == 5)),
#     )
# )

def getDifferentSolution(solut, md, *params):
    for p in params:
        solut.add(Or([p[i] != md.eval(p[i]) for i in range(len(p))]))

numsolutions = 0
while s.check() == sat:
    numsolutions += 1
    mod = s.model()
    print(mod)
    getDifferentSolution(s, mod, [x, y, z])

print('Number of solutions:', numsolutions)