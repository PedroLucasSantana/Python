# O datetime usa o ano, mes, data e horario do momento
from datetime import datetime
agora = datetime.now()
print(agora)

# Da pra pegar so o ano 
from datetime import datetime
agr = datetime.now()
print(agr.year)

# Da pra pegar so o mes 
from datetime import datetime
agr = datetime.now()
print(agr.month)

# Da pra pegar so o dia
from datetime import datetime
agr = datetime.now()
print(agr.day)

# Da pra pegar so a hora
from datetime import datetime
agr = datetime.now()
print(agr.hour)

# Da pra pegar so os minutos
from datetime import datetime
agr = datetime.now()
print(agr.minute)

# Da pra pegar so os segundos
from datetime import datetime
agr = datetime.now()
print(agr.second)

# Criando uma data manualmente
from datetime import datetime
aniver = datetime(2005, 8, 23)
print(aniver)

# Tambem é possivel informar a hora
from datetime import datetime
evento = datetime(2026, 12, 25, 18, 30)
print(evento)

# Dá pra formata a data
from datetime import datetime
agora = datetime.now()
print(agora.strftime("%d/%m/%Y"))