import math


def rho0(x, longueurSegment):
    if 0 <= x <= 1000:
        return 200
    elif 2000 <= x <= 3000:
        return 200
    else:
        return 0


def v(p, v_max):
    if p > 0:
        res = math.sqrt(7.716 * ((1000 / p) - 4))
        if res <= v_max:
            return res
        else:
            return v_max
    else:
        return v_max


def f(p, v_max):
    return p * v(p, v_max)


def gG(s1, s2, v_max, rho_max):
    if s1 <= rho_max / 2 and s2 <= rho_max / 2:
        return f(s1, v_max)
    elif s1 >= rho_max / 2 and s2 >= rho_max / 2:
        return f(s2, v_max)
    elif s1 < rho_max / 2 < s2:
        return min(f(s1, v_max), f(s2, v_max))
    else:
        return f(rho_max / 2, v_max)


def calcul(A, deltaT, deltaX, v_max, rho_max):
    l = deltaT / deltaX
    Y = [0 for i in range(len(A))]
    for i in range(1, len(A) - 1):
        Y[i] = A[i] - (l * (gG(A[i], A[i + 1], v_max, rho_max) - gG(A[i - 1], A[i], v_max, rho_max)))
    return Y
