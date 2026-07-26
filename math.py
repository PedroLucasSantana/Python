# valor de pi
import math
print(f"Valor de PI: {math.pi:.2f}")

# valor de um circulo
import math
raio = 5
area = math.pi * raio ** 2
print(f"Valor do área do circulo: {area}")

# Número de Euler
import math
print(f"Valor de Euler: {math.e:.3}")

# Numero tau
import math 
print(f"Valor de tau: {math.tau:.2f}")

# inf representa o infinito
import math
print(f"Valor infinito: {math.inf}")
# EXEMPLO usado para inicializar variáveis quando procura um valor menor
#OBS: tambem tem a opcao de um valor maior que utiliza o -math.inf e troca a <> 
menor = math.inf
numeros = [10, 3, 8, 1]
for numero in numeros:
    if numero < menor:
        menor = numero
print(f"Valor menor: {menor}")

# nan significado "não é um número"
import math
print(f"Valor nan: {math.nan}")
# EXEMPLO 
import math
joao = 8
maria = 10
pedro = math.nan
print('-----EXEMPLO NAN-----')
print(f"João: {joao}")
print(f"Maria: {maria}")
print(f"Pedro: {pedro}") # ele nao fez a prova ent aqui devia ter um numero como nao existe aplicamos o nan
print('---------------------')

# sqrt serve para calcular a raiz quadrada de um numero
import math
resultado = math.sqrt(25)
print(f"Raiz quadrada de 25: {resultado}")

# ciel ele arredonda um numero pra cima
import math
print(f"Valor aredondado pra cima: {math.ceil(4.2)}")

# floor ele arredonda um numero pra baixo
import math
print(f"Valor arredonda pra baixo: {math.floor(4.9)}")

# trunc ele remove a parte decimal de um numero
import math
print(f"Valor com o decimal cortado: {math.trunc(7.9)}")

# pow serve para elevar o numero a potencia
import math
print(f"Valor elevado a potencia: {math.pow(2, 3)}")
# no caso ele irá fazer 2x2x2=8

# factorial calcula o fatorial de um numero
import math
print(f"Fatorial do numero 5: {math.factorial(5)}")
# no caso irá fazer 5x4x3x2x1=120

# gcd ele encontra o maior numero que divide e nao deixa resto
import math
print(f"Numero que divide 12 e 18 sem deixar resto: {math.gcd(12, 18)}")

# isclose verifica se dois numero sao praticamentes iguais
import math
print(f"0.1 + 0.2 são considerados proximos: {math.isclose(0.1+0.2, 0.3)}")

# fabs retorna a distancia de um numero ate o zero, ignorando se ele e positivo ou negativo
import math
print(f"Valor absoluto de -20: {math.fabs(-20)}")

# log calcula o logaritmo natural
import math
print(f"Logaritmo natural de 10: {math.log(10)}")

# log2 calcula o logaritmo na base 2
import math
print(f"Logaritmo base 2 de 8: {math.log2(8)}")
# 2x2x2=8

# log10 calcula o logaritmo na base 10
import math
print(f"Logaritmo base 10 de 100: {math.log10(100)}")

# fsum soma numeros com maior precisao
import math
lista = [0.1, 0.2, 0.3]
print(f"Somando 0.1 + 0.2 + 0.3 = {math.fsum(lista)}")

# prod multiplica todos os numero de uma lista
import math 
lista2 = [2,3,4]
print(f"Multiplicando 2x3x4 = {math.prod(lista2)}")

# dist calcula a distancia entre dois numeros
import math
p1 = (0,0)
p2 = (3,4)
print(f"A distancia entre a p1 e p2 é: {math.dist(p1, p2)}")

# hypot calcula a hipotenusa de um triângulo retângulo
import math
print(f"A hipotenusa de 3 e 4: {math.hypot(3, 4)}")

# isnan verifica o nan
import math
nota = math.nan
if math.isnan(nota):
    print("Aluno sem nota")

# lcm calcula o MMC entre dois numeros
import math
print(f"O MMC de 12 e 18: {math.lcm(12, 18)}")

# exp ele eleva o numero de euler que é 2,71828
import math
print(f"Elevando em 2: {math.exp(2)}")
# e^2 = 2,71828 × 2,71828 = 7.389