# def soma(a, b):
#     c = a + b
#     if c % 2 == 0:
#         return "Par"
#     else:
#         return "Ímpar"

# print(soma(3, 6))

# def fatorial(n):
#     if n == 1:
#         return 1
#     return n * fatorial(n -1)

# print(fatorial(5))

# Desafio 1: Fazer o sistema de verificação de maioridade usando funções

# def calcularIdade():
#     anoNascimento = int(input("Digite seu ano de nascimento: "))
#     anoAtual = int(input("Digite o ano atual: "))
#     return anoAtual - anoNascimento

# def eMaiorDeIdade():
#     # idade = calcularIdade()
#     if calcularIdade() >= 18:
#         print("É maior")
#     else:
#         print("É menor")

# eMaiorDeIdade()


# Desafio 2: Fazer uma contagem de 0 a 10 usando recursão
# Fazer a mesma contagem de 10 a 0

# def contarAteDez(n):
#     if n == 10:
#         return n
#     else:
#         return f"{n} {contarAteDez(n + 1)}"

# def contarAteZero(n):
#     if n == 0:
#         return n
#     else:
#         return f"{n} {contarAteZero(n - 1)}"

def contarCrescente(inicio, fim):
    while inicio < fim:
        return f"{inicio} {contarCrescente(inicio + 1, fim)}"
        
    return inicio

# def contarCrescente(inicio, fim):
#     if inicio == fim:
#         return inicio
#     else:
#         return f"{inicio} {contarCrescente(inicio + 1, fim)}" 

def contarDecrescente(inicio, fim):
    while inicio > fim:
        return f"{inicio} {contarDecrescente(inicio -1, fim)}"
    
    return inicio

# def contarDecrescente(inicio, fim):
#     if inicio == fim:
#         return inicio
#     else:
#         return f"{inicio} {contarDecrescente(inicio - 1, fim)}" 

# print(contarAteDez(0))    
# print(contarAteZero(10))    
print(contarCrescente(0, 10))
print(contarDecrescente(10, 0))
