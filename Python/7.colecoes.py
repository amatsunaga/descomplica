# LISTA
# lista = [1, 2, 3]
# lista.append(4)
# lista.remove(2)
# lista.insert(1, 6)
# print(lista)

# TUPLA - imutável!
# tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# if 8 in tupla:
#     print("Existe")
# else:
#     print("Não existe")

# print(tupla[5])

# DICIONÁRIO - sem índice numérico
# dicionario = {"nome": "Marcio","sobrenome": "Santos"}
# print(dicionario["nome"], dicionario["sobrenome"])

# CONJUNTOS
# setA = {1, 3, 5, 6}
# setB = {1, 3}

# print(setA.intersection(setB))
# print(setA.difference(setB))
# print(setA.symmetric_difference(setB))
# print(setB.issubset(setA))
# print(setA.issuperset(setB))
# print(setA.isdisjoint(setB))

# DESAFIO
# Criar uma função recursiva (ou não) para verificar se o valor "Descomplica" está presente entre um dos nomes inseridos na lista.
# Se foi: exibir apenas o nome DESCOMPLICA
# Se não: exibir todos os nomes

def temDescomplica():
    nomes = []
    busca = {"descomplica"}

    for a in range(5):
        nomes.append((input("Nome: ")).casefold())

    if busca.issubset(nomes):
        return "DESCOMPLICA"
    else:
        return nomes

print(temDescomplica())


# def criarLista(n):
#     while n > 1:
#         nome = input("Nome: ")
#         return f"{nome} {criarLista(n - 1)}"      

#     return input("Nome: ")

# def temDescomplica():
#     nomes = criarLista(3).casefold().split(" ")
#     busca = {"descomplica"}
    
#     if set(nomes).issuperset(busca):
#         return "DESCOMPLICA"
#     else:
#         return nomes

# print(temDescomplica())

# Eficiência do código
# a = 10
# b = 20
# c = 30
# d = 40

# e = a + b + c + d

# Em caso de multiprocessamento (distribuído ou em paralelo), melhor:
# e = a + b
# f = c + d
# g = e + f

# print(g)