# As funções servem para organizar o código, evitar repetição e deixar programas mais profissionais.

# Exemplo Básico
def nome_da_funcao():
    print("Hello, World!!")
nome_da_funcao()

# Exemplo com parâmetros
def parametros(nome):
    print(f"Hello, {nome}!!")
parametros("Pedro")

# Exemplo com Soma
def soma(a, b):
    print(a + b)
soma(10, 5)

# Exemplo com return, o return ele guarda a função até ser chamada e ai sim ele executa
def soma2(g, h):
    return g + h
resultado = soma2(10, 2)
print(f"Valor da Soma: {resultado}")

# Exemplo com condições
def verificar_idade(idade):
    if idade >= 18:
        return "Maior de Idade"
    else:
        return "Menor de Idade"
print(verificar_idade(20))

# Exemplo com Loops 
def contar():
    for i in range(5):
        print(i)
contar()

# Exemplos Funções com Múltiplos Valores
def operacoes(a, b):
    soma3 = a + b
    sub = a - b
    return soma3, sub
re = operacoes(8, 2)
print(re)

# Argumentos Padrãos
def arg(nome="Visitante"):
    print(f"Hello, {nome}")
arg()

# Funções Recursivas
def conta(numero2):
    if numero2 == 0:
        return
    print(numero2)
    conta(numero2 - 1)
conta(10)

# Caso receba uma quantidade grande de valores
def valores(*numeros7):
    print(sum(numeros7))
valores(1, 2, 3, 4, 5)

# Caso receba uma quantidade grande de dados
def dados(**dados):
    print(dados)
dados(nome="Pedro", idade=20)

# Exemplo de Sistema
def calcular_media(notas):
    media = sum(notas) / len(notas)

    if media >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"

    return media, status


notas_aluno = [2, 1, 9]

media, resultado = calcular_media(notas_aluno)

print(f"Média: {media}")
print(f"Resultado: {resultado}")