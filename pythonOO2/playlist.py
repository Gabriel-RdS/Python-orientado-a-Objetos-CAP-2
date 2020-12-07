
class Playlist:

    def __init__(self, nome, programa):
        self.nome = nome
        self._programa = programa

    @property
    def tamanho(self):
        return len(self._programa)

    @property
    def listagem(self):
        return self._programa
