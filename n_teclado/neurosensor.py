from n_teclado.chave_ import ListaNeuronio
from n_teclado.camada_oculta.distribuicao_exec.camada1 import Camada1
from n_teclado.camada_oculta.processo_celular import ProcessoCelular

from universal.estruturaneuroniobase import NeuronioBase

from BANCO_DADOS.lista_teclas_pt import Teclas
from BANCO_DADOS.lista_neuronio import ListaNeuronio_db

from TERMINAL_SISTEMA.acesso import Terminal
from TERMINAL_SISTEMA.comandos import ComandosInternos

class Sensor:
    
    
    def __init__(self):

        while ProcessoCelular.loop_Sensor:

            print("**" * 20)
            print("Sinara\n")

            inter = input("digite uma informação: ")

            if inter == ComandosInternos.comand_cd:

               terminal = Terminal()

            else:

                enter = ListaNeuronio() 
                energia_celular = NeuronioBase()

                len_inter = len(inter)
                

                #for com inter
                for ent in range (0,len_inter):

                    va = Teclas.teclas_return(inter)

                    if va == None:

                        print("letra não indentificado: ", inter[ent])
                        print("encerando sistema.")
                        ProcessoCelular.loop_Sensor = False

                neuronio = ListaNeuronio_db()
                neuronio.neuronio_tabela()

                

                print("entrada: ",enter.neuronio_entrada)
                prox = Camada1()      

    

        