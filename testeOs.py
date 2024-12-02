import os # interagir com o sistema
import platform #clique

arquivos = os.listdir('.') # lista tudo do diretório indicado
print(arquivos)

print("**** aqui meu diário! ****")

arquivo = open("diarioAWS.txt", "w")
arquivo.write("Hoje estamos mais um dia de python")
arquivo.close()
arquivos = os.listdir('.')
print(arquivos)

print("#### lendo o arquivo ####")
arquivo = open("diarioAWS.txt", "r")
print(arquivo.read())
arquivo.close()
# comando os.system permite executar comandos de terminal
os.system("ls -la")# saída no terminal pelo comando ls
os.chmod("diarioAWS.txt",0o700)#mudar para 700
print("\n**** alteração do arquivo ****")
os.system("ls -la")

#os.chmod("diarioAWS.txt",stat.S_IRWXU)#mudar para 700
#print("\n**** alteração para o dono do arquivo ****")
#os.system("ls -la")

print("adicionando novo diretorio")
os.mkdir("diretorioNovo2") #cria um novo diretório
os.system("ls -la")

os.rmdir("diretorioNovo") #apaga um diretorio indicado
os.remove("diarioAWS.txt") # apaga um arquivo indicado
os.system("ls -la")