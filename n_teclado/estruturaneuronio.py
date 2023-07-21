from n_teclado.neurosensor import Sensor
from n_teclado.processo_celular import ProcessoCelular
from n_teclado.chave.chave_ import ChaveInicial
from n_teclado.chave.chave_entrada import ChaveEntrada

from TERMINAL_SISTEMA.comandos import ComandosInternos
from TERMINAL_SISTEMA.acesso import Terminal

from BANCO_DADOS.pasta_entrada.lista_teclas_pt import Teclas

class Neuronio:

    def __init__(self):

        while ProcessoCelular.loop_Sensor:

            print("**" * 20)
            print("Sinara\n")

            inter = input("digite uma informação: ")

            if inter == ComandosInternos.comand_cd:

               Terminal()

            else:
                
                var_if = 0

                while_t = True
                soma_while = 0

                #for com inter
                while while_t: ## verificar string
                    
                    tec = Teclas()
                    va = tec.teclas_return(inter[soma_while])
                        
                    if va == None:

                        tec.teclas_inserir(inter[soma_while])

                        va = tec.teclas_return(inter[soma_while])

                        var_if = va[0]

                        ProcessoCelular.processo_entrada = []

                    elif va[0] > var_if:

                        var_if = va[0]

                    soma_while = soma_while + 1
                    
                    if soma_while == len(inter):

                        while_t = False
                            
                len_index = len(ProcessoCelular.processo_entrada)
                print("len,var",len_index, var_if)

                CE_ = ChaveEntrada()

                if var_if > len_index:
                    
                    CE_.init_insert()

                    CE_.init_rede_entrada()

                self.sensor_trabalho(inter) ## entrada

    def sensor_trabalho(self,inter):

        sensory = Sensor()
        sensory.sensor_iniciar(inter)

        
                            
    
                            
        