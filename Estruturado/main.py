from calculos import (
    calcular_delta,
    calcular_pontos,
    calcular_raizes,
    calcular_vertice,
)
from entrada import obter_coeficientes
from grafico import mostrar_grafico
from resultados import mostrar_resultados


def main():
    a, b, c = obter_coeficientes()
    delta = calcular_delta(a, b, c)
    raizes = calcular_raizes(a, b, c, delta)
    vertice = calcular_vertice(a, b, c, delta)
    pontos = calcular_pontos(a, b, c)

    mostrar_resultados(a, b, c, delta, raizes, vertice)
    mostrar_grafico(a, b, c, pontos, vertice, raizes)


if __name__ == "__main__":
    main()
