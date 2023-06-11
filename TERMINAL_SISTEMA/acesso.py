
from n_teclado.camada_oculta.processo_celular import ProcessoCelular

from TERMINAL_SISTEMA.comandos import ComandosInternos

from BANCO_DADOS.lista_teclas_pt import Teclas
class Terminal:

    def __init__(self) -> None:
        
        print("\nAcessando sistema:")
        inp = input("sistema interno: {} ".format(ComandosInternos.comand_cd))

        if inp == "ut avertas": ## latin: desligar

            print("Desligando sistema.")

            ProcessoCelular.loop_Sensor = False

        elif inp == "inserere littera":

            yper = input('escolha uma letra: ')
            Teclas.teclas_inserir(yper)

        