# Em vez de escolher manualmente, o import randint escolhe aleatoriamente pra voce
import random
numero = random.randint(1, 10)
print(f"Meu número aleatório é: {numero}")

# O randrange escolhe um numero aleatorio excluindo o ultimo
import random
numero2 = random.randrange(0, 10)
print(f"Numero escolhido: {numero2}")

# O random escolhe um numero decimal entre 0.0 e 1.0
import random
print(f"Número decimal: {random.random()}")

# O choice escolhe um unico elemento dentro de uma lista
import random
nomes = ['Pedro', 'Petrus', 'Marya']
print(f"O nome escolhido foi: {random.choice(nomes)}")

# O sample escolhe um unico elemento sem repetir os elementos
import random
nomes2 = ['Pedro', 'Petrus', 'Marya']
print(f"Os dois nomes dessa vez foi: {random.sample(nomes2, 2)}")

# O shuffle embaralha uma lista
import random
n = [1, 2, 3, 4, 5]
random.shuffle(n)
print(f"Os numeros embaralhados são: {n}")