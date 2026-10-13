import math


def _ler_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem).strip().replace(",", "."))
            if not math.isfinite(valor):
                raise ValueError
            return valor
        except ValueError:
            print("Entrada invalida. Digite um numero valido, por exemplo 2,5.")


def obter_coeficientes():
    a = _ler_numero("Digite o coeficiente a (diferente de zero): ")
    while a == 0:
        print("Entrada invalida: o coeficiente a nao pode ser zero. Tente novamente.")
        a = _ler_numero("Digite o coeficiente a (diferente de zero): ")

    b = _ler_numero("Digite o coeficiente b: ")
    c = _ler_numero("Digite o coeficiente c: ")
    return a, b, c