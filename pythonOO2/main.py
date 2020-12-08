from filme import Filme
from serie import Serie
from playlist import Playlist


def inicia_programa():
    vingadores = Filme("vingadores guerra inifinita", 2018, 160)
    batman_cdt = Filme("Batman: o Cavaleiro das trevas", 2008, 152)
    friends = Serie("frieds", 1994, 10)
    breaking_bad = Serie("breaking bad", 2008, 5)

    vingadores.dar_likes(533)
    batman_cdt.dar_likes(1223)
    friends.dar_likes(633)
    breaking_bad.dar_likes(841)

    lista_de_programas = [vingadores, batman_cdt, friends, breaking_bad]
    playlist_fds = Playlist("Programas", lista_de_programas)

    for programas in playlist_fds:
        print(programas)

    print(f'O tamanho da minha Playlist é de: {len(playlist_fds)} Programas')


if __name__ == "__main__":
    inicia_programa()
