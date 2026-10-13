from calculos import Calculos
from entrada import Entrada
from grafico import Grafico
from resultados import Resultados


def main():
    """Funcao principal que inicia a execucao do programa e orquestra as classes."""
    a, b, c = Entrada().obter_coeficientes()
    calculos = Calculos(a, b, c)

    delta = calculos.calcular_delta()
    raizes = calculos.calcular_raizes(delta)
    vertice = calculos.calcular_vertice(delta)
    pontos = calculos.calcular_pontos()

    Resultados().mostrar_resultados(a, b, c, delta, raizes, vertice)
    Grafico().mostrar_grafico(a, b, c, pontos, vertice, raizes)


if __name__ == "__main__":
    main()