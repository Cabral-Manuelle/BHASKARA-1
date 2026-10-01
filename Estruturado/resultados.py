def mostrar_resultados(a, b, c, delta, raizes, vertice):
    print("\nResultados da equacao:")
    print(f"Equacao: {a:g}x^2 + {b:g}x + {c:g} = 0")
    print(f"Delta: {delta:g}")

    if raizes is None:
        print("Raizes reais: nao existem (delta negativo).")
    else:
        print(f"Raiz x1: {raizes[0]:g}")
        print(f"Raiz x2: {raizes[1]:g}")

    print(f"Vertice: ({vertice[0]:g}, {vertice[1]:g})")