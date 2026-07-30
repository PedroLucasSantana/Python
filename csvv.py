# lendo um csv
import csv
with open("pessoas.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

# ignorando o cabeçalho
import csv
with open("pessoas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)
    for linha in leitor:
        print(linha)

# Acessando colunas
import csv
with open("pessoas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)
    for linha in leitor:
        nome = linha[0]
        idade = linha[1]
        print(f"{nome} tem {idade} anos")

# criando um csv
import csv
with open("dados.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Idade"])
    escritor.writerow(["Pedro", 20])
    escritor.writerow(["Maria", 25])

# escrevendo varias linhas de uma vez
import csv
dados = [
    ["Pedro", 20],
    ["Maria", 25],
    ["João", 30]
]
with open("dados.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Idade"])
    escritor.writerows(dados)

# adicionando novas linhas
import csv
with open("dados.csv", "a", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Carlos", 40])