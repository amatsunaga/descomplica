# erro: "bug", sintaxe incorreta, gera aviso na tela
# falha: não gera aviso, mas se comporta de maneira não esperada, diferente do planejado, é um erro lógico
# exceção: funciona em um cenário, mas em outro não (ex. divisão por zero)

# a = int(input("Digite um número: "))
# b = int(input("Digite outro número: "))

# if b == 0:
#     print("Não é possível dividir nenhum número por zero")
# else:
#     resultado = a / b
#     print(resultado)
    
try:
    print("Execute isso")
except:
    print("Uma exceção ocorreu")

