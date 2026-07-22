# A variable is a space in memory used to store information.

# EXAMPLE 1
name = "Pedro"
print(f'My name is {name}')

# EXAMPLE 2
age = 18
print(f'I am {age} years old')

# EXAMPLE 3
# The variable can change
age = 18
age = 19
print(f'I am {age} years old')

# Viable types
# 1. ( STR ) ela sempre vai ficar dentro das aspas.
str = "Pedro"
# 2. ( INT ) Será um número inteiro.
int = 2
# 3. ( FLOAT ) Será um número decimal.
altura = 1.75
# 4. ( Bool ) Será verdairo ou falso.
ativo = True

# Descobrindo o tipo da variável.
idade = 18
print(type(idade))

# Variáveis de Cálculos
# 1. Soma
x = 10
y = 5
soma = x + y
print(soma)
# 2. Subtração
x = 7
y = 2
subtracao = x - y 
print(subtracao)
# 3. Multiplicação
x = 10
y = 2
multiplicacao = x * y
print(multiplicacao)
# 4. Divisão
x = 20
y = 4
divisao = x / y
print(divisao)

# As variáveis támbem podem receber dados do usuário

# EXAMPLE 1
name = input(f"Digite seu nome: ")
print(f"Welcome {name}!")

# EXAMPLE 2
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
soma = numero1 + numero2
print(f"A soma é {soma}")
