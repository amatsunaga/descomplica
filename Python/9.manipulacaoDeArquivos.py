# r = read
# w = write
# x = execute
# a = append
# rwx r+ = read and write
# wb = write binary

# ARQUIVOS LOCAIS

# open("teste.txt", "x")

# conteudo = open("arquivo.txt", "a")
# conteudo.write("\nUma linha qualquer\n")
# conteudo.write("\nSegunda linha\n")
# conteudo.close()

# conteudo = open("arquivo.txt", "r")
# print(conteudo.read())
# print(conteudo.readline())

## outros comandos para manipular o conteÚdo de um arquivo aberto
# readline(n)
# readlines(n)
# replace()


# MANIPULAÇÃO DOS ARQUIVOS EM SI
# import os

# os.remove("teste.txt")
# os.mkdir("teste")
# os.rmdir("teste")


# ARQUIVOS EM NUVEM

# import requests

# ler = requests.get("https://wiki.sj.ifsc.edu.br/images/4/4a/Ecoshower.txt")
# # print(ler)

# with open("arquivo001.txt", "wb") as arquivo:
#     arquivo.write(ler.content)

    
