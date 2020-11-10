from itertools import permutations
from math import sqrt, pow

def is_valide(a, b, c):
    if (a >= (b+c)) or (b >= (a+c)) or (c >= (a+b)):
        return False
    else :
        return True

def aire_ordonne(a, b, c):
    if is_valide(a, b, c):
        ordered_list = sorted([a, b, c])
        u1, u2, u3 = ordered_list[0], ordered_list[1], ordered_list[2]
        aire = 0.5*sqrt(u1*u1*u3*u3 - pow(((u1*u1 - u2*u2 + u3*u3)/2), 2))
        return aire
    else:
        return 'les trois valeurs ne peuvent pas définir un triangle'

def perimettre(a, b, c):
    if is_valide(a, b, c):
        return a+b+c
    else:
        return 'les trois valeurs ne peuvent pas définir un triangle'

def nb_triangles_speciaux(n, p):
    perm = permutations(range(n, p+1), 3)
    l = [set(p) for p in perm]
    new_list = []
    for i in l :
        if i not in new_list:
            new_list.append(i)


    valide_list = [tuple(item) for item in new_list]
    valide_list = [item for item in valide_list if is_valide(item[0], item[1], item[2])]
    valide_list = [item for item in valide_list if aire_ordonne(item[0], item[1], item[2])==perimettre(item[0], item[1], item[2])]
    return len(valide_list)
nb_triangles_speciaux(1, 20)

print(nb_triangles_speciaux(1, 20))
