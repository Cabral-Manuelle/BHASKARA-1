# Bhaskara

Três implementações em Python para explorar a equação do segundo grau `ax² + bx + c = 0`. Cada versão calcula o discriminante, as raízes reais e o vértice da parábola; as versões de terminal também exibem o gráfico.

## Versões

| Pasta | Abordagem | Interação |
| --- | --- | --- |
| `Estruturado` | Funções organizadas por módulo | Terminal e gráfico Matplotlib |
| `OOP` | Classes organizadas por responsabilidade | Terminal e gráfico Matplotlib |
| `OOP_Janelas` | Classes com interface Tkinter | Janela interativa com resultados e gráfico |

## Requisitos

- Python 3.11
- Matplotlib
- Tkinter para `OOP_Janelas` (normalmente incluído na instalação do Python para Windows)

Abra o PowerShell na raiz deste repositório, a pasta `Bhaskara`, e instale o Matplotlib:

```powershell
py -3.11 -m pip install -r Estruturado/requirements.txt
```

## Executar

Rode um comando por vez, ainda a partir da raiz do repositório.

### Estruturado

```powershell
py -3.11 Estruturado/main.py
```

Usa funções para calcular os resultados e solicita os coeficientes no terminal.

### OOP

```powershell
py -3.11 OOP/main.py
```

Encapsula os cálculos e a apresentação em classes; a entrada dos coeficientes é feita no terminal.

### OOP_Janelas

```powershell
py -3.11 OOP_Janelas/main.py
```

Abre uma interface Tkinter para informar os coeficientes, configurar o intervalo e visualizar os resultados e o gráfico. O tema inicial da interface e do gráfico é violeta; também é possível escolher outros temas para o gráfico.

## Comparação

- **Estruturado:** fluxo direto e fácil de acompanhar, adequado para apresentar a decomposição procedural do problema.
- **OOP:** agrupa estado e comportamento em classes, favorecendo a separação de responsabilidades.
- **OOP_Janelas:** mantém a organização orientada a objetos e acrescenta uma interface gráfica, tornando a interação mais visual, com o custo de gerenciar widgets e eventos.
