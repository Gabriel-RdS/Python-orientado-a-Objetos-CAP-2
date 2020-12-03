from programa import Programa


class Serie(Programa):

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.__temporada = temporada

    @property
    def temporada(self):
        return self.__temporada
