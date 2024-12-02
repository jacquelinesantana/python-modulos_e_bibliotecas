import requests # requisições
'''
essa biblioteca requer instalação previa para funcionar
executar no terminal comando 'pip instal requests'
'''
response = requests.get("https://api.github.com")#envia requisição via get para o endereço

print(response.status_code)# retorno da requisição 