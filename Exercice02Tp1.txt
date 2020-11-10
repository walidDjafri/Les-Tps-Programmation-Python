from math import sqrt, pow
def is_valide(a, b, c):
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return False
    else:
        return True

def aire_ordonne(a, b, c):
    if is_valide(a, b, c):
        ordered_list = sorted([a, b, c])
        u1, u2, u3 = ordered_list[0], ordered_list[1], ordered_list[2]
        aire = 0.5*sqrt(u1*u1*u3*u3 - pow(((u1*u1 - u2*u2 + u3*u3)/2), 2))
        return aire
    else:
        return 'les trois valeurs ne peuvent pas définir un triangle'

aire_ordonne(3,4,5)
print(aire_ordonne(3,4,5))

aire_ordonne(13,14,15)
print(aire_ordonne(13,14,15))

aire_ordonne(1,1,1)
print(aire_ordonne(1,1,1))
