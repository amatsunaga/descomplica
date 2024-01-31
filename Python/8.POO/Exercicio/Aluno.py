from datetime import date

class Aluno:
    __nome = ""
    __anoNascimento = date.today().year

    def calcularIdade(self):
        idade = date.today().year - self.__anoNascimento
        return idade
    
    def __init__(self, nome, anoNascimento):
        self.__nome = nome
        self.__anoNascimento = anoNascimento