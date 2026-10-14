usuarios_A = {
    "Ana",
    "Carlos",
    "Joao",
    "Maria"
}

usuarios_B = {
    "Carlos",
    "Maria",
    "Pedro"
}

todos = usuarios_A | usuarios_B

comuns = usuarios_A & usuarios_B

print("Todos os usuarios:")
print(todos)

print("\nUsuarios nos dois sistemas:")
print(comuns)
