from filme import Filme
from serie import Serie


def inicia_programa():

    filme1 = Filme("vingadores: guerra inifinita", 2018, 160)
    serie1 = Serie("frieds", 1994, 10)

    print(f'Nome do Filme: {filme1.nome} - Data de Lançamento: {filme1.ano} - Duração: {filme1.duracao} min')
    print(f'Nome do Filme: {serie1.nome} - Data de Lançamento: {serie1.ano} - Duração: {serie1.temporada} temp')


if __name__ == "__main__":
    inicia_programa()
