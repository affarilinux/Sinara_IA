
from n_teclado.processo_celular import ProcessoCelular
from n_teclado.processo_celular import ProcessoCelular

from TERMINAL_SISTEMA.comandos import ComandosInternos

from BANCO_DADOS.lista_teclas_pt import Teclas
class Terminal:

    def __init__(self) -> None:
        
        print("\nAcessando sistema:")

        while ProcessoCelular.loop_sistema_ineterno:
            
            inp = input("sistema interno: {} ".format(ComandosInternos.comand_cd))

            if inp == "*ire":

                ProcessoCelular.loop_sistema_ineterno = False
            
            elif inp == "ut avertas": ## latin: desligar

                print("Desligando sistema.")

                ProcessoCelular.loop_Sensor = False
                ProcessoCelular.loop_sistema_ineterno = False

            elif inp == "character inserere":

                yper = input('escolha um caractere: ')

                teclas_ = Teclas()
                teclas_.teclas_inserir(yper)

        