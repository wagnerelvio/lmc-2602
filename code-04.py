'''
Comparacoes de arquivos
'''

servidor_A = {
    "dados.csv",
    "clientes.txt",
    "relatorio.pdf",
    "config.json"
}

servidor_B = {
    "dados.csv",
    "clientes.txt",
    "backup.zip",
    "usuarios.csv"
}

# Arquivos presentes nos dois servidores

comuns = servidor_A & servidor_B

# Arquivos existentes somente no servidor A

somente_A = servidor_A - servidor_B

# Arquivos diferentes entre os servidores

diferentes = servidor_A ^ servidor_B

print("Arquivos comuns:")
print(comuns)

print("\nSomente no servidor A:")
print(somente_A)

print("\nArquivos diferentes:")
print(diferentes)
