
class Filme:
    def __init__(self, nome, lancamento, duracao):
        self.__nome = nome.title()
        self.__lancamento = lancamento
        self.__duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def lancamento(self):
        return self.__lancamento

    @property
    def duracao(self):
        return self.__duracao
