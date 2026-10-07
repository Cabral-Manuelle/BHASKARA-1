from tkinter import ttk


class Resultados:
    def __init__(self, parent):
        self.delta_texto = ttk.Label(
            parent, text="Delta: -", style="Resultado.TLabel"
        )
        self.raizes_texto = ttk.Label(
            parent,
            text="Raízes reais: -",
            style="Resultado.TLabel",
            wraplength=240,
        )
        self.vertice_texto = ttk.Label(
            parent, text="Vértice: -", style="Resultado.TLabel"
        )

        self.delta_texto.pack(anchor="w", pady=3)
        self.raizes_texto.pack(anchor="w", pady=3)
        self.vertice_texto.pack(anchor="w", pady=3)

    def mostrar_resultados(
        self, delta, raizes, vertice, mostrar_raizes=True, mostrar_vertice=True
    ):
        self.delta_texto.configure(text=f"Delta: {delta:g}")

        if not mostrar_raizes:
            texto_raizes = "Raízes: ocultas"
        elif raizes is None:
            texto_raizes = "Raízes reais: não existem (delta negativo)."
        else:
            texto_raizes = f"Raizes: x1 = {raizes[0]:g} e x2 = {raizes[1]:g}"
        self.raizes_texto.configure(text=texto_raizes)
        if mostrar_vertice:
            texto_vertice = f"Vértice: ({vertice[0]:g}, {vertice[1]:g})"
        else:
            texto_vertice = "Vértice oculto"
        self.vertice_texto.configure(text=texto_vertice)

    def limpar(self):
        self.delta_texto.configure(text="Delta: -")
        self.raizes_texto.configure(text="Raízes reais: -")
        self.vertice_texto.configure(text="Vértice: -")