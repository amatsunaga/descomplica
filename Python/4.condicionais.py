# idade = int(input("Digite sua idade: "))

# if idade > 18:
#     print("É maior de idade")
# elif idade == 18:
#     print("É Guerreiro Jedi")
# else:
#     print("É MENOR de idade")


# print("É MAIOR") if idade >=18 else print("É MENOR")


# a = "Marcio"
# match a:
#     case "Antonio":
#         print("Não é Marcio")
#     case "Pedro":
#         print("É Pedro e não Marcio")
#     case "Marcio":
#         sobrenome = input("Digite seu sobrenome: ")
#         print(a, sobrenome)

anoNascimento = int(input("Digite seu ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))
idade = anoAtual - anoNascimento

if idade >=18:
    input("Digite seu título de eleitor: ")
else:
    input("Digite o CPF do responsável: ")