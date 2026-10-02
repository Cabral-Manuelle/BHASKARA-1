# Calculadora de Bhaskara

Projeto com três implementações para calcular a equação do segundo grau $ax^2 + bx + c = 0$. As versões calculam o discriminante ($\Delta$), as raízes e o vértice da parábola; também exibem o gráfico.

## Requisitos

- Python 3.11
- Matplotlib
- Tkinter para a versão com janelas. No Windows, o Tkinter normalmente acompanha a instalação padrão do Python.

No PowerShell, execute os comandos a partir da raiz deste repositório (`Bhaskara`). Instale a dependência uma vez:

```powershell
py -3.11 -m pip install -r Estruturado/requirements.txt
```

## Como executar

### Estruturado

Implementação procedural: as funções de cálculo recebem os coeficientes e retornam os resultados.

```powershell
py -3.11 Estruturado/main.py
```

### OOP

Implementação orientada a objetos: classes organizam os cálculos, a entrada de dados, os resultados e o gráfico.

```powershell
py -3.11 OOP/main.py
```

### OOP_Janelas

Implementação orientada a objetos com interface gráfica Tkinter. Informe os coeficientes na janela para visualizar os resultados e o gráfico.

```powershell
py -3.11 OOP_Janelas/main.py
```

## Comparação das abordagens

- **Estruturado:** fluxo direto com funções e dados passados entre módulos; é simples de acompanhar para um programa pequeno.
- **OOP:** agrupa comportamentos e dados em classes, favorecendo a organização por responsabilidades e a evolução do código.
- **OOP_Janelas:** reutiliza a organização orientada a objetos e acrescenta uma interface gráfica, tornando a interação mais visual, com maior complexidade de interface.
