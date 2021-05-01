import math


def rho0(x, longueurSegment):
    """if 0 <= x < longueurSegment // 10:
        return x
    elif longueurSegment // 10 <= x < longueurSegment // 5:
        return 200 - x
    else:
        return 0"""

    """if 0 <= x < 500:
        return 100
    elif 1000 <= x < 1500:
        return 200
    else:
        return 0"""

    """if 0 <= x < longueurSegment // 20:
        return 200
    elif longueurSegment // 20 <= x < 2 * longueurSegment // 20:
        return 0
    elif 2 * longueurSegment // 20 <= x < 3 * longueurSegment // 20:
        return 200
    elif 3 * longueurSegment // 20 <= x < 4 * longueurSegment // 20:
        return 0
    elif 4 * longueurSegment // 20 <= x < 5 * longueurSegment // 20:
        return 200
    else:
        return 0"""

    if 0 <= x < 1000:
        return 200
    else:
        return 0


def v(p, v_max, rho_max):
    return (v_max / rho_max) * (rho_max - p)


def f(p, v_max, rho_max):
    return p * v(p, v_max, rho_max)


def gG(s1, s2, v_max, rho_max):
    if s1 <= rho_max / 2 and s2 <= rho_max / 2:
        return f(s1, v_max, rho_max)
    elif s1 >= rho_max / 2 and s2 >= rho_max / 2:
        return f(s2, v_max, rho_max)
    elif s1 < rho_max / 2 < s2:
        return min(f(s1, v_max, rho_max), f(s2, v_max, rho_max))
    else:
        return f(rho_max / 2, v_max, rho_max)


def calcul(A, deltaT, deltaX, v_max, rho_max):
    l = deltaT / deltaX
    Y = [0 for i in range(len(A))]
    for i in range(1, len(A) - 1):
        Y[i] = A[i] - (l * (gG(A[i], A[i + 1], v_max, rho_max) - gG(A[i - 1], A[i], v_max, rho_max)))
    return Y


def calculerNormeErreur(liste, deltaX):
    result = 0
    for i in range(len(liste)):
        result = result + (liste[i]) ** 2
    result = result * deltaX
    result = math.sqrt(result)
    return result
