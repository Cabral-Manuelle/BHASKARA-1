import matplotlib.pyplot as plt


class Grafico:
    def mostrar_grafico(self, a, b, c, pontos, vertice, raizes):
        x_valores, y_valores = pontos
        figura, eixo = plt.subplots()
        eixo.plot(x_valores, y_valores, label="y = ax^2 + bx + c", color="teal")
        eixo.scatter(*vertice, color="darkorange", zorder=3, label="Vertice")
        eixo.annotate(
            "Vertice", vertice, xytext=(8, 8), textcoords="offset points"
        )

        if raizes is not None:
            eixo.scatter(
                list(raizes),
                [0] * len(raizes),
                color="crimson",
                zorder=3,
                label="Raizes",
            )

        eixo.axhline(0, color="black", linewidth=0.8)
        eixo.axvline(0, color="black", linewidth=0.8)
        eixo.set_title(f"Grafico de y = {a:g}x^2 + {b:g}x + {c:g}")
        eixo.set_xlabel("x")
        eixo.set_ylabel("y")
        eixo.grid(True, alpha=0.3)
        eixo.legend()
        figura.tight_layout()
        plt.show()