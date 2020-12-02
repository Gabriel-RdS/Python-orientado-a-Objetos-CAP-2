from filme import Filme
from serie import Serie


def inicia_programa():

    filme1 = Filme("vingadores: guerra inifinita", 2018, 160)
    serie1 = Serie("frieds", 1994, 10)

    print(f"Nome do Filme: {filme1.nome} - Data de lançamento: {filme1.lancamento} "
          f"- Duração: {filme1.duracao} minutos")

    print(f"Nome da Serie: {serie1.nome} - Data de lançamento: {serie1.lancamento} "
          f"- Duração: {serie1.temporada} temporadas")


if __name__ == "__main__":
    inicia_programa()
