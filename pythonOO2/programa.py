
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self, numero_de_likes=1):
        self._likes += numero_de_likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, value):
        self._ano = value

    def __str__(self):
        return f'Nome do Filme: {self._nome} - Data de Lançamento: {self._ano} - Likes: {self._likes} likes'
