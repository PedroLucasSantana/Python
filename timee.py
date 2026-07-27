# Essa função faz o programa pausar por alguns segundos
import time
print("Começando...")
time.sleep(3)
print("Terminou!")

# O time retorna o numero de segundos desde 1 de janeiro de 1970
import time
print(time.time())

# O ctime converte o timestamp em uma data mais facil de ler
import time
print(time.ctime())

# O localtime retorna varias informações sobre a data e a hora
import time
agora = time.localtime()
print(agora)