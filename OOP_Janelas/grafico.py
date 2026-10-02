from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class Grafico:
    def __init__(self, parent):
        self.figura = Figure(figsize=(6, 5), dpi=100)
        self.eixo = self.figura.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figura, master=parent)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        self._mostrar_vazio()

    def _mostrar_vazio(self):
        self.eixo.set_xlabel("x")
        self.eixo.set_ylabel("y")
        self.eixo.grid(True, alpha=0.3)
        self.canvas.draw()

    def mostrar_grafico(
        self,
        a,
        b,
        c,
        pontos,
        vertice,
        raizes,
        tema="roxo",
        mostrar_grade=True,
        mostrar_raizes=True,
        mostrar_vertice=True,
    ):
        x_valores, y_valores = pontos
        cores = {
            "roxo": {
                "fundo": "#f4efff",
                "texto": "#302345",
                "grade": "#d7c7f5",
                "curva": "#7041c7",
                "vertice": "#e07a3f",
                "raizes": "#cb3d70",
            },
            "claro": {
                "fundo": "#ffffff",
                "texto": "#263238",
                "grade": "#cbd5d9",
                "curva": "#087f75",
                "vertice": "#d8751b",
                "raizes": "#c43d55",
            },
            "escuro": {
                "fundo": "#202a33",
                "texto": "#edf2f2",
                "grade": "#59656e",
                "curva": "#54d2c2",
                "vertice": "#ffc16b",
                "raizes": "#ff788b",
            },
        }
        paleta = cores.get(tema, cores["roxo"])
        self.figura.set_facecolor(paleta["fundo"])
        self.eixo.set_facecolor(paleta["fundo"])
        self.eixo.clear()
        self.eixo.set_facecolor(paleta["fundo"])
        self.eixo.plot(
            x_valores,
            y_valores,
            label="y = ax^2 + bx + c",
            color=paleta["curva"],
        )

        if mostrar_vertice:
            self.eixo.scatter(
                *vertice,
                color=paleta["vertice"],
                zorder=3,
                label="Vertice",
            )

        if mostrar_raizes and raizes is not None:
            self.eixo.scatter(
                list(raizes),
                [0] * len(raizes),
                color=paleta["raizes"],
                zorder=3,
                label="Raizes",
            )

        self.eixo.axhline(0, color=paleta["texto"], linewidth=0.8)
        self.eixo.axvline(0, color=paleta["texto"], linewidth=0.8)
        self.eixo.set_title(f"y = {a:g}x^2 + {b:g}x + {c:g}")
        self.eixo.set_xlabel("x")
        self.eixo.set_ylabel("y")
        self.eixo.tick_params(colors=paleta["texto"])
        self.eixo.xaxis.label.set_color(paleta["texto"])
        self.eixo.yaxis.label.set_color(paleta["texto"])
        self.eixo.title.set_color(paleta["texto"])
        for borda in self.eixo.spines.values():
            borda.set_color(paleta["grade"])
        if mostrar_grade:
            self.eixo.grid(True, color=paleta["grade"], alpha=0.55)
        else:
            self.eixo.grid(False)
        if mostrar_vertice or (mostrar_raizes and raizes is not None):
            legenda = self.eixo.legend()
            legenda.get_frame().set_facecolor(paleta["fundo"])
            legenda.get_frame().set_edgecolor(paleta["grade"])
            for texto in legenda.get_texts():
                texto.set_color(paleta["texto"])
        self.figura.tight_layout()
        self.canvas.draw_idle()