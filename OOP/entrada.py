class Entrada:
    def _ler_numero(self, mensagem):
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("Digite um numero valido.")

    def obter_coeficientes(self):
        a = self._ler_numero("Digite o coeficiente a (diferente de zero): ")
        while a == 0:
            print("O coeficiente a nao pode ser zero.")
            a = self._ler_numero("Digite o coeficiente a (diferente de zero): ")

        b = self._ler_numero("Digite o coeficiente b: ")
        c = self._ler_numero("Digite o coeficiente c: ")
        return a, b, c