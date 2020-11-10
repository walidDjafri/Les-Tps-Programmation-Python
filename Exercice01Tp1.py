""" Enoncé :
Donner une définition, avec signature et
hypothèse(s) éventuelle(s), de la fonction isocele
qui, étant donné trois nombres positifs a, b et c
définissant les trois côtés d’un triangle, renvoie le
booléen vrai si ce triangle est isocèle, le booléen
faux sinon. (L’expression “définissent les trois côtés
d’un triangle” vise à exclure des valeurs telles que a
= 1, b = 1, c = 20 qui ne permettent pas de tracer un
triangle, car c est “trop grand” par rapport aux deux
autres valeurs.)
Exemple :
>>> isocele(4, 2, 3) => False
>>> isocele(4, 3, 3) => True
>>> isocele(4, 4, 4) => True  """


def is_valide(a, b, c):
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return False
    else:
        return True

def is_isocelle(a, b, c):
    if is_valide(a, b, c):
        if len({a, b, c}) <= 2:
            return True
        else:
            return False
    else:
        return 'les trois valeurs ne peuvent pas définir un triangle'

is_isocelle(2,2,1)
print(is_isocelle(2,2,1))

is_isocelle(2,2,2)
print(is_isocelle(2,2,2))

is_isocelle(2,4,1)
print(is_isocelle(2,4,1))
