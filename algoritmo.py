# Um algoritmo é uma sequência de passos para resovler um problema ou executar uma tarefa.

# Exercício de um sistema escolar.
alunos = [
    {"nome": "Pedro", "nota": 9},
    {"nome": "Marya", "nota": 6},
    {"nome": "Petrus", "nota": 8},
]
print("--Sistema Escolar--")
for aluno in alunos:
    if aluno["nota"] >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"
    print(f"{aluno["nome"]} - {status}")

# Exercício de Identificar se é maior de idade
pessoas = [
    {"nome": "Pedro", "idade": 20},
    {"nome": "Marya", "idade": 16},
    {"nome": "Petrus", "idade": 25}
]
print()
print("--Sistema de Idade--")
for pessoa in pessoas:
    if pessoa["idade"] >= 18:
        status = "Maior de idade"
    else:
        status = "Menor de idade"
    print(f"{pessoa["nome"]} - {status}")

# Exercício de controle de estoque.
estoque = [
    {"nome": "Mouse", "quant": 20},
    {"nome": "Teclado", "quant": 0},
    {"nome": "Monitor", "quant": 5}
]

print()
print("--Sistema de Estoque--")
for est in estoque:
    if est["quant"] > 0:
        status = "Disponível"
    else:
        status = "Sem Estoque"
    print(f"{est["nome"]} - {status}")

# Exercício de Soma de notas.
usuarios = [
    {"nome": "Pedro", "nota": 10},
    {"nome": "Marya", "nota": 5},
    {"nome": "Petrus", "nota": 8}
]

print()
print("--Sistema de Soma--")
soma = 0
for usu in usuarios:
    soma += usu["nota"]
print(f"Soma de todas as notas foi {soma}")

turma = [
    {"nome": "Luciano", "nota": 5},
    {"nome": "Danilo", "nota": 2},
    {"nome": "Leticia", "nota": 9}
]

print()
print("--Sistema para Encontrar a Maior Nota--")
maiornota = turma[0]
for aluno in turma:
    if aluno["nota"] > maiornota["nota"]:
        maiornota = aluno
print(f"Aluno: {maiornota['nome']} / Nota: {maiornota['nota']}")

turma2 = [
    {"nome": "Samuel", "nota": 8},
    {"nome": "Miro", "nota": 2},
    {"nome": "Luciano", "nota": 9},
    {"nome": "Gabriel", "nota": 3},
    {"nome": "Gabrielzinho", "nota": 4}
]

print()
print("--Sistema de Aprovados e Reprovados--")
aprovados = []
reprovados = []
for aluno in turma2:
    if aluno['nota'] >= 7:
        aprovados.append(aluno['nome'])
    else:
        reprovados.append(aluno['nome'])
print(f"Alunos APROVADOS: {', '.join(aprovados)}")
print(f"Alunos REPROVADOS: {', '.join(reprovados)}")