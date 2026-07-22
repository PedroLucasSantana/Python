# LISTAS é uma coleção ordenada de itens.
# Exemplo
compras = ["Arroz", "Feijão", "Macarrão", "Leite"]

# DICIONÁRIO guarda dados em pares
# Exemplo
pessoa = {
    "nome": "Pedro",
    "idade": 20,
    "cidade": "Rio de Janeiro"
}

# Como acessar a posição de uma lista
nomes = ["Pedro", "João"]
print(nomes[0])

# Como acessar por chave no dicionário
pessoa = {
    "nome": "Lucas"
}
print(pessoa["nome"])

# OBS: Quando devo usar a lista? R: Quando a ordem IMPORTAR
# OBS: Quando devo usar a dicionário? R: Quando cada informação possui uma descrição

# Como alterar o valor de uma lista
frutas = ["Maçã", "Banana", "Laranja"]
frutas[1] = "Uva"
print(frutas)

# Como remover elementos de uma lista
frutas2 = ["Maçã", "Banana", "Laranja"]
frutas2.remove("Laranja")
print(frutas2)

# Como saber o tamanho de uma lista
print(len(frutas2))

# Loop em Lista 
frutas4 = ["Manga", "Banana", "Uva Verde"]
for fruta in frutas4:
    print(fruta)

# Acessando valores no Dicionário
pessoa8 = {
    "nome": "Pedro",
    "idade": 20,
    "cidade": "Saquarema" 
}

print(pessoa8["nome"])

# Alterando Valores no Dicionário
pessoa8["idade"] = 22

# Adicionando Dados no Dicionário
pessoa8["profissao"] = "Programador"

# Removendo do Dicionário
del pessoa8["cidade"]

# Feita as Alterações
print(pessoa8)

# Loop em Dicionário
for chave in pessoa8:
    print(chave)

# Chamando a chave e o valor do dicionário
for chave, valor in pessoa8.items():
    print(chave, valor)

# Uma lista de Dicionários
usuarios = [
    {
        "nome": "Petrus",
        "idade": 7
    },
    {
        "nome": "Marya",
        "idade": 19
    }
]

# Acessando a lista de dicionário
print(usuarios[1]["nome"])

# Sistema de Cadastro 
usuarios2 = []
usu = {
    "nome": "Pedro",
    "idade": 20,
    "email": "pedro@email.com"
}
usuarios2.append(usu)

# Buscando usuário 
for usu in usuarios2:
    if usu["nome"] == "Pedro":
        print(usu)

# EXERCÍCIO EXTRA
alunos = [
    {
        "nome": "Pedro",
        "nota": 9
    },
    {
        "nome": "Marya",
        "nota": 8
    },
    {
        "nome": "Petrus",
        "nota": 7
    }
]
for aluno in alunos:
    print(f"Aluno: {aluno["nome"]} - Nota: {aluno["nota"]}")