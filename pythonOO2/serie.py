from programa import Programa


class Serie(Programa):

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self._temporada = temporada

    @property
    def temporada(self):
        return self._temporada

    def __str__(self):
        return f'Nome da série: {self.nome} - Duração: {self._temporada} Temporadas ' \
               f'Quantidade de Likes: {self.likes}'
