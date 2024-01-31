class Animal:
    def __init__(self, nome, cor):
        self.__nome = nome
        self.__cor = cor

    def comer(self):
        print(f"O {self.__nome} está comendo")

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cor(self):
        return self.__cor
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cor.setter
    def cor(self, cor):
            self.__cor = cor