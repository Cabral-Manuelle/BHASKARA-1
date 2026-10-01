def _ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um numero valido.")


def obter_coeficientes():
    a = _ler_numero("Digite o coeficiente a (diferente de zero): ")
    while a == 0:
        print("O coeficiente a nao pode ser zero.")
        a = _ler_numero("Digite o coeficiente a (diferente de zero): ")

    b = _ler_numero("Digite o coeficiente b: ")
    c = _ler_numero("Digite o coeficiente c: ")
    return a, b, c