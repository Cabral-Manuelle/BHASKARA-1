import math


class Calculos:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def _validar_a(self):
        if self.a == 0:
            raise ValueError("O coeficiente a nao pode ser zero.")

    def calcular_delta(self):
        return self.b**2 - 4 * self.a * self.c

    def calcular_raizes(self, delta=None):
        self._validar_a()
        if delta is None:
            delta = self.calcular_delta()
        if delta < 0:
            return None

        raiz_delta = math.sqrt(delta)
        return (
            (-self.b + raiz_delta) / (2 * self.a),
            (-self.b - raiz_delta) / (2 * self.a),
        )

    def calcular_vertice(self, delta=None):
        self._validar_a()
        if delta is None:
            delta = self.calcular_delta()

        x_vertice = -self.b / (2 * self.a)
        y_vertice = -delta / (4 * self.a)
        return x_vertice, y_vertice

    def calcular_pontos(self, quantidade=201):
        self._validar_a()
        delta = self.calcular_delta()
        x_vertice, _ = self.calcular_vertice(delta)
        distancia_raiz = math.sqrt(abs(delta)) / (2 * abs(self.a))
        meia_largura = max(2.0, distancia_raiz * 1.25)
        quantidade = max(2, int(quantidade))

        x_inicial = x_vertice - meia_largura
        passo = (2 * meia_largura) / (quantidade - 1)
        x_valores = [x_inicial + indice * passo for indice in range(quantidade)]
        y_valores = [self.a * x**2 + self.b * x + self.c for x in x_valores]
        return x_valores, y_valores