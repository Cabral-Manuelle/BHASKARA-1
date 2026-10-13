class Entrada:
    """Classe responsavel por gerir a entrada de dados do utilizador."""
    def _ler_numero(self, mensagem):
        """Le um numero validando se a entrada do utilizador esta correta."""
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("Digite um numero valido.")

    def obter_coeficientes(self):
        """Solicita e retorna os coeficientes a, b e c da equacao."""
        a = self._ler_numero("Digite o coeficiente a (diferente de zero): ")
        while a == 0:
            print("O coeficiente a nao pode ser zero.")
            a = self._ler_numero("Digite o coeficiente a (diferente de zero): ")

        b = self._ler_numero("Digite o coeficiente b: ")
        c = self._ler_numero("Digite o coeficiente c: ")
        return a, b, c