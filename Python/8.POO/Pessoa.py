class Pessoa:
    #encapsulamento:
    # _nome não deve ser alterado (apenas convenção, não dá erro). parecido com protected
    # __nome não pode ser acessado fora da classe (private)
    __nome = "Marcio"
    _idade = 38
    passos = 5

    def exibir(self):
        print(self.__nome, self._idade)

    def caminhar(self, passos):
        self.passos += passos
        return self.passos

    # não existe sobreposição/ sobrecarga e sobrescrita em python. então não funciona escrever 2 métodos com o mesmo nome
    # def adicionar(self, tamanho, cor):
    #     pass

    # def adicionar(self, voltagem, cor, dimensoes):
    #     pass

    def __init__(self, nome, idade):
        self.__nome = nome
        self._idade = idade

    # def __init__(self):
    #     i = self._idade
    #     n = self.__nome

    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        self._idade = idade    