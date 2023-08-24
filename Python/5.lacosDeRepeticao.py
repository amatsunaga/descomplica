# WHILE
# a = 1

# while a < 10:
#     print("Teste")
#     a += 1

# FOR
# for a in range(5):
#     print("marcio")

# a = ["Marcio", "Larissa", "Benedito", "André"]
# for a in a:
#     print(a)

# a = "Descomplica"
# for a in a:
#     print(a)

# a = []
# b = 1
# print(a)
# while b <=3:
#     a.append(input("Digite um nome de aluno: "))
#     b += 1
# print(a)

# a = ["Marcio", "Bruna"]
# a.insert(1, "Hellen")
# print(a)
# a.remove("Marcio")
# print(a)

# DESENVOLVER ALGORITMO
# Diretor cadastra alunos com os dados:
# Nome, CPF, email, matrícula
# Para cada aluno cadastrado, o diretor pode lançar 3 notas
# Se a média atingida for maior ou igual a 6, escrever:
# Aluno X, vocë foi aprovado. Seu diploma terá os seguintes dados:
# listar todos os dados do aluno
# Caso a média seja inferior a 6, lançar uma nota adicional e tirar nova média
# Senão, aluno reprovado.

alunos = []
i = 0

class Aluno:
    def __init__(self, nome, cpf, email, matricula):
        self.nome = nome,
        self.cpf = cpf,
        self.email = email,
        self.matricula = matricula,
        self.notas = [],
        self.media = 0

    def __repr__(self):
        return f"Aluno {self.nome}, CPF {self.cpf}, e-mail {self.email}, matrícula {self.matricula}, notas: {self.notas}, média final: {self.media}"

while i < 3:
    nome = input("Digite o nome do aluno: ")
    cpf = input("Digite o CPF do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")

    aluno = Aluno(nome, cpf, email, matricula)

    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))

    aluno.notas = [nota1, nota2, nota3]
    aluno.media = (aluno.notas[0] + aluno.notas[1] + aluno.notas[2]) / len(aluno.notas)

    alunos.append(aluno)

    if aluno.media >= 6:
        print(f"Aluno {aluno.nome}, você foi aprovado. O diploma terá os seguintes dados: \n CPF: {aluno.cpf}, e-mail: {aluno.email}, matrícula: {aluno.matricula}")
    else:
        nota4 = int(input("Adicione a nota de recuperação: "))
        aluno.notas = [nota1, nota2, nota3, nota4]
        aluno.media = (aluno.notas[0] + aluno.notas[1] + aluno.notas[2] + aluno.notas[3]) / len(aluno.notas)

        if aluno.media >= 6:
            print(f"Aluno {aluno.nome}, você foi aprovado. O diploma terá os seguintes dados: \n CPF: {aluno.cpf}, e-mail: {aluno.email}, matrícula: {aluno.matricula}")
        else:
            print("Aluno reprovado.")

    i += 1

