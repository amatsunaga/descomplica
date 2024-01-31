from Pessoa import Pessoa

# pessoa2 = Pessoa()
# pessoa1 = Pessoa()
pessoa2 = Pessoa("Andrea", 37)

# print(pessoa.nome)
# print(pessoa.idade)

# pessoa.exibir("Marcio", 38)
# pessoa1.exibir("Benedito", 42)

# pessoa.exibir()
# print(pessoa.__nome)
pessoa2.exibir()

pessoa2.nome = "Maria"
pessoa2.idade = 41
pessoa2.exibir()
print(pessoa2.caminhar(10))