import math


def rho0(x, longueurSegment):
    """if 0 <= x < longueurSegment // 10:
        return x
    elif longueurSegment // 10 <= x < longueurSegment // 5:
        return 200 - x
    else:
        return 0"""
    if 0 <= x < longueurSegment // 10:
        return 200
    else:
        return 0


def v(p, v_max):
    return v_max


def f(p, v_max):
    return p * v(p, v_max)


def gG(s1, s2, v_max):
    return f(s1, v_max)


def calcul(A, deltaT, deltaX, v_max):
    l = deltaT / deltaX
    Y = [0 for i in range(len(A))]
    for i in range(1, len(A) - 1):
        Y[i] = A[i] - (l * (gG(A[i], A[i + 1], v_max) - gG(A[i - 1], A[i], v_max)))
    return Y


def rhoTheorique(x, t, v_max, longueurSegment):
    return rho0(x - v_max * t, longueurSegment)


def calculerNormeErreur(liste, deltaX):
    result = 0
    for i in range(len(liste)):
        result = result + (liste[i]) ** 2
    result = result * deltaX
    result = math.sqrt(result)
    return result
