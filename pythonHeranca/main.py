from junior import Junior
from pleno import Pleno


def inicia_programa():

    jose = Junior('José')
    jose.busca_perguntas_sem_resposta()
    print('\n')

    luan = Pleno('Luan')
    luan.busca_perguntas_sem_resposta()
    luan.busca_cursos_do_mes()
    print('\n')

    # Se nos comentarmos a função mostrar_tarefas() da classe alura, nossa resposta será da classe Caelum
    luan.mostrar_tarefas()
    print('\n')

    # Pleno herdou a classe hipster
    print(luan)
    # Junior NÃO herdou a classe hipster
    print(jose)


if __name__ == "__main__":
    inicia_programa()
