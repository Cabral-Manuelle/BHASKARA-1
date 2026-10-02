import math
from tkinter import BooleanVar, messagebox, ttk


class Entrada:
    def __init__(self, parent, ao_calcular):
        self.ao_calcular = ao_calcular
        self.frame = ttk.LabelFrame(parent, text="Parametros", padding=12)
        self.campos = {}
        valores_iniciais = {
            "a": "1",
            "b": "-3",
            "c": "2",
            "x_min": "-10",
            "x_max": "10",
            "quantidade": "401",
        }

        parametros = (
            ("a", "Coeficiente a"),
            ("b", "Coeficiente b"),
            ("c", "Coeficiente c"),
            ("x_min", "Inicio do eixo x"),
            ("x_max", "Fim do eixo x"),
            ("quantidade", "Quantidade de pontos"),
        )
        for linha, (chave, rotulo) in enumerate(parametros):
            ttk.Label(self.frame, text=rotulo).grid(
                row=linha, column=0, sticky="w", padx=(0, 12), pady=5
            )
            campo = ttk.Entry(self.frame, width=18)
            campo.insert(0, valores_iniciais[chave])
            campo.grid(row=linha, column=1, sticky="ew", pady=5)
            self.campos[chave] = campo

        ttk.Label(self.frame, text="Tema do grafico").grid(
            row=6, column=0, sticky="w", padx=(0, 12), pady=5
        )
        self.tema = ttk.Combobox(
            self.frame,
            values=("Roxo", "Claro", "Escuro"),
            state="readonly",
            width=15,
        )
        self.tema.current(0)
        self.tema.grid(row=6, column=1, sticky="ew", pady=5)

        self.mostrar_grade = BooleanVar(value=True)
        self.mostrar_raizes = BooleanVar(value=True)
        self.mostrar_vertice = BooleanVar(value=True)
        ttk.Checkbutton(
            self.frame, text="Mostrar grade", variable=self.mostrar_grade
        ).grid(row=7, column=0, columnspan=2, sticky="w", pady=3)
        ttk.Checkbutton(
            self.frame, text="Mostrar raizes", variable=self.mostrar_raizes
        ).grid(row=8, column=0, columnspan=2, sticky="w", pady=3)
        ttk.Checkbutton(
            self.frame, text="Mostrar vertice", variable=self.mostrar_vertice
        ).grid(row=9, column=0, columnspan=2, sticky="w", pady=3)

        self.frame.columnconfigure(1, weight=1)
        ttk.Button(
            self.frame,
            text="Calcular",
            command=self._enviar_coeficientes,
        ).grid(row=10, column=0, columnspan=2, sticky="ew", pady=(12, 0))

    def _enviar_coeficientes(self):
        try:
            a, b, c, x_min, x_max = (
                float(self.campos[chave].get())
                for chave in ("a", "b", "c", "x_min", "x_max")
            )
            quantidade = int(self.campos["quantidade"].get())
        except ValueError:
            messagebox.showerror(
                "Entrada invalida",
                "Use numeros validos e uma quantidade inteira de pontos.",
            )
            return

        if not all(math.isfinite(valor) for valor in (a, b, c, x_min, x_max)):
            messagebox.showerror(
                "Entrada invalida", "Os valores devem ser numeros finitos."
            )
            return

        if a == 0:
            messagebox.showerror("Entrada invalida", "O coeficiente a nao pode ser zero.")
            self.campos["a"].focus_set()
            return
        if x_min >= x_max:
            messagebox.showerror(
                "Intervalo invalido", "O inicio do eixo x deve ser menor que o fim."
            )
            return
        if not 2 <= quantidade <= 10000:
            messagebox.showerror(
                "Quantidade invalida",
                "A quantidade de pontos deve estar entre 2 e 10000.",
            )
            return

        opcoes = {
            "tema": self.tema.get().lower(),
            "mostrar_grade": self.mostrar_grade.get(),
            "mostrar_raizes": self.mostrar_raizes.get(),
            "mostrar_vertice": self.mostrar_vertice.get(),
        }
        self.ao_calcular(a, b, c, x_min, x_max, quantidade, opcoes)