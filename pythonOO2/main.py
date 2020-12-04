from filme import Filme
from serie import Serie


def inicia_programa():
    filme1 = Filme("vingadores guerra inifinita", 2018, 160)
    serie1 = Serie("frieds", 1994, 10)

    # Polimorfismo
    playlist_de_programa = [filme1, serie1]
    for programa in playlist_de_programa:
        print(programa)


if __name__ == "__main__":
    inicia_programa()
