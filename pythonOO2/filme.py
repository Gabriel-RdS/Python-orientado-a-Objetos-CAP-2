from programa import Programa


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao

    def __str__(self):
        return f'Nome da série: {self.nome} - Duração: {self._duracao} min ' \
               f'Quantidade de Likes: {self.likes}'
