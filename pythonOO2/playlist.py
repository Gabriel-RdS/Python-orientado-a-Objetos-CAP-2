
class Playlist:

    def __init__(self, nome, programa):
        self.nome = nome
        self._programa = programa

    # Permite eu iterar meu objeto como se fosse uma lista
    # duck typing
    def __getitem__(self, item):
        return self._programa[item]

    # Permite eu iterar meu objeto com a função len() fora da classe
    # duck typing
    def __len__(self):
        return len(self._programa)

    @property
    def listagem(self):
        return self._programa
