from string import Template

nome = input("Digite seu nome: ")
nascimento = input("Qual seu ano de nascimento? ")
email = input("Digite seu e-mail: ")

# CONCATENAÇÃO
print("Nome:", nome, ". E-mail:", email, ". Nascimento:", nascimento)

# Literal string interpolation/ f-strings - powerful, easy to use, increases readability
print(f'Nome: {nome}. E-mail: {email}. Nascimento: {nascimento}.')

# Str.format() - simple positional formatting
print("Nome: {}.".format(nome), "E-mail: {}.".format(email), "Nascimento: {}".format(nascimento))
print("Nome: {nome}. E-mail: {email}. Nascimento: {nascimento}".format(nome=nome, email=email, nascimento=nascimento))

# Simple string interpolation - Não recomendado pois é um método antigo e que dificulta a leitura do código
print("Nome: %s. E-mail: %s. Nascimento: %s." %(nome, email, nascimento))
print("Nome: %(nome)s. E-mail: %(email)s. Nascimento: %(nascimento)s." %{"nome": nome, "email": email, "nascimento": nascimento})

# Template string
new = Template("Nome: $nome. E-mail: $email. Nascimento: $nascimento.")
print(new.substitute(nome=nome, email=email, nascimento = nascimento))

# print("Nome: ")
# print(nome)
# print("Nascimento: ")
# print(nascimento)
# print("E-mail: ")
# print(email)

# Tratamento da entrada de dados/ parse / conversáo de tipos
a = int(input("Digite um número: "))
print(a + 5)

