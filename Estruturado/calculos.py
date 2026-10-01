import math


def _validar_a(a):
    if a == 0:
        raise ValueError("O coeficiente a nao pode ser zero.")


def calcular_delta(a, b, c):
    return b**2 - 4 * a * c


def calcular_raizes(a, b, c, delta=None):
    _validar_a(a)
    if delta is None:
        delta = calcular_delta(a, b, c)
    if delta < 0:
        return None

    raiz_delta = math.sqrt(delta)
    return (-b + raiz_delta) / (2 * a), (-b - raiz_delta) / (2 * a)


def calcular_vertice(a, b, c, delta=None):
    _validar_a(a)
    if delta is None:
        delta = calcular_delta(a, b, c)

    x_vertice = -b / (2 * a)
    y_vertice = -delta / (4 * a)
    return x_vertice, y_vertice


def calcular_pontos(a, b, c, quantidade=201):
    _validar_a(a)
    delta = calcular_delta(a, b, c)
    x_vertice, _ = calcular_vertice(a, b, c, delta)
    distancia_raiz = math.sqrt(abs(delta)) / (2 * abs(a))
    meia_largura = max(2.0, distancia_raiz * 1.25)
    quantidade = max(2, int(quantidade))

    x_inicial = x_vertice - meia_largura
    passo = (2 * meia_largura) / (quantidade - 1)
    x_valores = [x_inicial + indice * passo for indice in range(quantidade)]
    y_valores = [a * x**2 + b * x + c for x in x_valores]
    return x_valores, y_valores
