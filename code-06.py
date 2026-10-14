'''
Produto cartesiano
'''

import matplotlib.pyplot as plt
from itertools import product

# Definindo os conjuntos
A = {1, 2, 3}
B = {2, 4, 6}

# Calculando o produto cartesiano
AxB = list(product(sorted(A), sorted(B)))

# Exibindo os pares ordenados
print("Produto cartesiano A x B:")
for par in AxB:
    print(par)

# Separando coordenadas X e Y
x = [par[0] for par in AxB]
y = [par[1] for par in AxB]

# Criando o gráfico
plt.figure(figsize=(8, 6))

plt.scatter(x, y, color="blue", s=100)

# Identificando os pares ordenados
for xi, yi in AxB:
    plt.annotate(
        f"({xi},{yi})",
        (xi, yi),
        xytext=(5, 8),
        textcoords="offset points"
    )

plt.title("Produto Cartesiano A x B")
plt.xlabel("Conjunto A - Eixo X")
plt.ylabel("Conjunto B - Eixo Y")

plt.xticks(sorted(A))
plt.yticks(sorted(B))

plt.xlim(0, 4)
plt.ylim(0, 7)

plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
