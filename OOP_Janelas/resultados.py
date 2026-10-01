from tkinter import ttk


class Resultados:
    def __init__(self, parent):
        self.delta_texto = ttk.Label(parent, text="Delta: -")
        self.raizes_texto = ttk.Label(parent, text="Raizes reais: -", wraplength=240)
        self.vertice_texto = ttk.Label(parent, text="Vertice: -")

        self.delta_texto.pack(anchor="w", pady=3)
        self.raizes_texto.pack(anchor="w", pady=3)
        self.vertice_texto.pack(anchor="w", pady=3)

    def mostrar_resultados(
        self, delta, raizes, vertice, mostrar_raizes=True, mostrar_vertice=True
    ):
        self.delta_texto.configure(text=f"Delta: {delta:g}")

        if not mostrar_raizes:
            texto_raizes = "Raizes: ocultas"
        elif raizes is None:
            texto_raizes = "Raizes reais: nao existem (delta negativo)."
        else:
            texto_raizes = f"Raizes: x1 = {raizes[0]:g} e x2 = {raizes[1]:g}"
        self.raizes_texto.configure(text=texto_raizes)
        if mostrar_vertice:
            texto_vertice = f"Vertice: ({vertice[0]:g}, {vertice[1]:g})"
        else:
            texto_vertice = "Vertice: oculto"
        self.vertice_texto.configure(text=texto_vertice)