from abc import ABCMeta, abstractmethod


class Programa(metaclass=ABCMeta):
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

    # Permite eu iterar meu objeto como uma string
    # Um método abstrato pois, sempre será sobrescrito nas minha subclasses, e não podera ser ->
    # -> iterado na minha classe mãe
    @abstractmethod
    def __str__(self):
        pass
