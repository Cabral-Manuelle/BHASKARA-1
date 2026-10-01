import tkinter as tk
from tkinter import messagebox, ttk

from calculos import Calculos
from entrada import Entrada
from grafico import Grafico
from resultados import Resultados


def main():
    janela = tk.Tk()
    janela.title("Bhaskara - Equacao do segundo grau")
    janela.geometry("1080x720")
    janela.minsize(900, 600)

    estilo = ttk.Style(janela)
    estilo.configure("Titulo.TLabel", font=("Segoe UI", 18, "bold"))
    estilo.configure("Subtitulo.TLabel", font=("Segoe UI", 10))

    painel = ttk.Frame(janela, padding=18)
    painel.grid(row=0, column=0, sticky="ns")
    area_grafico = ttk.Frame(janela, padding=(0, 18, 18, 18))
    area_grafico.grid(row=0, column=1, sticky="nsew")
    janela.columnconfigure(1, weight=1)
    janela.rowconfigure(0, weight=1)
    area_grafico.rowconfigure(0, weight=1)
    area_grafico.columnconfigure(0, weight=1)

    ttk.Label(painel, text="Bhaskara", style="Titulo.TLabel").pack(anchor="w")
    ttk.Label(
        painel,
        text="Calculadora de equacao do segundo grau",
        style="Subtitulo.TLabel",
        wraplength=270,
    ).pack(anchor="w", pady=(2, 16))

    quadro_entrada = ttk.Frame(painel)
    quadro_entrada.pack(fill="x")
    quadro_resultados = ttk.LabelFrame(painel, text="Resultados", padding=12)
    quadro_resultados.pack(fill="x", pady=(16, 0))

    resultados = Resultados(quadro_resultados)
    grafico = Grafico(area_grafico)

    def calcular(a, b, c, x_min, x_max, quantidade, opcoes):
        try:
            calculos = Calculos(a, b, c)
            delta = calculos.calcular_delta()
            raizes = calculos.calcular_raizes(delta)
            vertice = calculos.calcular_vertice(delta)
            pontos = calculos.calcular_pontos(x_min, x_max, quantidade)
        except ValueError as erro:
            messagebox.showerror("Erro no calculo", str(erro), parent=janela)
            return

        resultados.mostrar_resultados(
            delta,
            raizes,
            vertice,
            opcoes["mostrar_raizes"],
            opcoes["mostrar_vertice"],
        )
        grafico.mostrar_grafico(
            a,
            b,
            c,
            pontos,
            vertice,
            raizes,
            opcoes["tema"],
            opcoes["mostrar_grade"],
            opcoes["mostrar_raizes"],
            opcoes["mostrar_vertice"],
        )

    entrada = Entrada(quadro_entrada, calcular)
    entrada.frame.pack(fill="x")

    janela.mainloop()


if __name__ == "__main__":
    main()