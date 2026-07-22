# Conditions in python are used by programmers to make decisions.

# EXAMPLE 
idade = 18
print(idade >= 18)

# Some examples of comparison operators
# 1. == IGUAL / EXAMPLE: X == 10
# 2. != DIFERENTE / EXAMPLE: X != 5
# 3. > MAIOR / EXAMPLE: X > 8
# 4. < MENOR / EXAMPLE: X < 3
# 5. >= MAIOR OU IGUAL / EXAMPLE: X >= 18
# 6. <= MENOR OU IGUAL / EXAMPLE: X <= 100

# Structure IF
idade = 20
if idade >= 18:
    print("Are you of legal age!")

# Structure ELSE 
idade = 15
if idade >= 18:
    print("Are you of legal age!")
else:
    print("Are you not of legal age!")

# Structure ELIF
nota = 7
if nota >= 9:
    print("Excellent")
elif nota >= 7:
    print("Approved")
else:
    print("failed")

# Logical Operators 
# 1. AND / Significado: E
idade = 18
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode Dirigir")
# 2. OR / Significado: OU
dinheiro = 100
cartao = False

if dinheiro >= 50 or cartao:
    print("Compra permitida")
# 3. NOT / Significado: NÃO
logado = False
if not logado:
    print("Faça login")

# EXAMPLE
# 1.
    usuario = "Pedro"
    senha = "1234"

    if usuario == "Pedro" and senha == "1234":
        print("Login realizado")
    else:
        print("Usuário ou senha incorretos")
# 2.
    nota = 8
    frequencia = 80

    if nota >= 7 and frequencia >= 75:
        print("Aluno aprovado")

    elif nota >= 5:
        print("Recuperação")

    else:
        print("Reprovado")

# Condições dentro de Condições
# 1.
    idade = 20
    tem_documento = True

    if idade >= 18:

        if tem_documento:
            print("Entrada permitida")

        else:
            print("Precisa apresentar documento")

    else:
        print("Menor de idade")