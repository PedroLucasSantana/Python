# transformar dicionario em json
import json
pessoa = {
    "nome": "Pedro",
    "idade": 20
}
json_texto = json.dumps(pessoa)
print(json_texto)

# Transformar JSON em dicionário
import json
texto_json = '{"nome":"Pedro","idade":20}'
dados = json.loads(texto_json)
print(dados)
print(dados["nome"])

# Salvar JSON em um arquivo
import json
usuario = {
    "nome": "Pedro",
    "idade": 20
}
with open("usuario.json", "w") as arquivo:
    json.dump(usuario, arquivo)
print("Arquivo criado!")

#Ler JSON de um arquivo
import json
with open("usuario.json", "r") as arquivo:
    dados = json.load(arquivo)
print(dados)

# Trabalhando com listas
import json
nomes = [
    "Pedro",
    "Maria",
    "João"
]
resultado = json.dumps(nomes)
print(resultado)

# Exemplo parecido com API
import json
resposta_api = '''
{
    "nome": "Pedro",
    "idade": 20,
    "cidade": "Saquarema"
}
'''
dados = json.loads(resposta_api)
print(dados["nome"])
print(dados["cidade"])