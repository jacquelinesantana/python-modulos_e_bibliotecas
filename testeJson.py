# json
import json # biblioteca que permite trabalhar com documentos formatados para json

# Criamos a estrutura do arquivo com os dados 
dados = {
    "nome": "Alice",
    "idade":25,
    "habilidades":["Python", "Javascript", "Java"]
}

# with esta aqui pra gerenciar o recurso que nesse caso é um arquivo
'''
O with é usado para gerenciar recursos, como arquivos, 
conexões a bancos de dados ou blocos de código que exigem 
inicialização e finalização controladas. Ele garante que os 
recursos serão corretamente liberados ou finalizados, mesmo 
que ocorra uma exceção dentro do bloco.

Vantagens do with:
Garante que o arquivo será fechado, mesmo em caso de erro.
O código fica mais legível e menos propenso a erros.

'''
with open("dadosAWS.json", "w") as arquivo: 
    json.dump(dados, arquivo, indent=4) #dump é a função que permite gravar dados no arquivo
    #dados -> informação do documento
    #arquivo -> arquivo que vai ser gravada a informação
    #indent -> identação do arquivo
    
print("Dados salvos no arquivo.")


with open("dadosAWS.json","r") as arquivo:
    dados_carregados = json.load(arquivo) #função load le o arquivo
    
    print("resultado do arquivo:")
    print(dados_carregados)