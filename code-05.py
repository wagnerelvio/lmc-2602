A = {1, 2, 3}
B = {"a", "b"}

produto = set()

for x in A:
    for y in B:
        produto.add((x, y))

print("Produto cartesiano:")

for par in produto:
    print(par)
