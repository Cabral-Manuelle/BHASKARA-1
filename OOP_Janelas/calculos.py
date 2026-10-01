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

    def calcular_pontos(self, x_min, x_max, quantidade=201):
        self._validar_a()
        if not math.isfinite(x_min) or not math.isfinite(x_max) or x_min >= x_max:
            raise ValueError("O intervalo deve conter valores finitos e inicio menor que fim.")
        if not isinstance(quantidade, int) or not 2 <= quantidade <= 10000:
            raise ValueError("A quantidade de pontos deve ser um inteiro entre 2 e 10000.")

        passo = (x_max - x_min) / (quantidade - 1)
        x_valores = [x_min + indice * passo for indice in range(quantidade)]
        y_valores = [self.a * x**2 + self.b * x + self.c for x in x_valores]
        return x_valores, y_valores