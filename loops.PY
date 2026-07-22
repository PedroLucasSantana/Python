# Loops servem para repetir ações automaticamente.

# Exemplos sem loop
# print("-- Sem Loop --")
# print("Hello")
# print("Hello")
# print("Hello")

# Exemplos com loop
# print("-- Com Loop --")
# for i in range(3):
#   print("Hello")
#    break

# Exemplos, a contagem vai do 0 ao 4 porque o python conta o 0 também.
# for i range(5):
#   print(i)

# Exemplos, aqui estamos falando do python pra começar do 1 e ir até o 6 e seguindo a mesma regra de cima.
# for i range(1, 6):
#    print(i)

# Exemplos, aqui irá começar do 0 irá terminar no 10, pulando de 2 em 2.
# for i range(0, 10, 2):
#   print(i)

# Exemplos, agora terá um loop regrassivo.
# for i in range(1-, 0, -1):
#   print(i)

# Exemplos, For com Listas
# frutas = ["maçã", "banana", "uva"]
# for fruta in frutas:
#   print(fruta)

# Exemplos, For com Tuplas
# numeros = [1, 2, 3]
# for n in numeros:
#   print(n)

# Exemplos, For com Dicionários
# pessoa = {
#    "nome": "Pedro",
#    "idade": 20
#}
# for chave in pessoa:
#   print(chave)

# Loop While se repete enquanto uma condição for verdadeira.

# Estrutura do WHILE
# while condicao:
#    codigo

# Exemplos Simples, o contador ele tem que ser menor 5 e começar do 1.
# contador = 1
# while contador <= 5:
#   print(contador)
#   contador += 1

# Como parar um while, usando o break
# Exemplo
# while True:
#   texto = input("Digite sair: ")
#   if texto == "sair":
#       break

# Outro Exemplo
# for i in range(10):
#   if i == 5:
#       break
#   print(i)

# Existe o pass, serve como espaço reservado e não faz nada.
# for i in range(5):
#   pass

# Loop dentro de Loop
# for i in range(3):
#   for j in range(3):
#       print(i, j)

# Aplicação Real com uma Tabuada
# numero = int(input("Digite um número: "))
# for i in range(1, 11):
#   print(f"{numero} x {i} = {numero * i}")

# Aplicação Real com um Sistema de Login
# senha = ""
# while senha != "1234":
#   senha = input("Digite a senha: ")
# print("Acesso Permitido")

# Aplicação Real com um sistema de Soma de Valores
# soma = 0
# for i in range(5):
#   numero = int(input("Digite um número: "))
#   soma += numero
# print(f"Total: {soma}")

# Um Sistema de Menu
#while True:

#    print("""
#1 - Ver usuários
#2 - Adicionar usuário
#3 - Sair
#""")

#    opcao = input("Escolha: ")

#    if opcao == "1":
#        print("Mostrando usuários")

#    elif opcao == "2":
#        print("Adicionando usuário")

#    elif opcao == "3":
#        print("Saindo...")
#        break

#    else:
#        print("Opção inválida")