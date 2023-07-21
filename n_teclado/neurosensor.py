
from n_teclado.processo_celular import ProcessoCelular

from BANCO_DADOS.pasta_entrada.lista_teclas_pt import Teclas


class Sensor:
    
    def sensor_iniciar(self,inter):

        tec1 = Teclas()

        for lein in range(0,len(inter)): ## ler a string texto

            ## ordem tabela banco ## qual letra
            vai = tec1.teclas_return(inter[lein]) 

            ler1 = len(ProcessoCelular.processo_entrada[vai[0]-1])## qual sublista
            
            for lein1 in range(0,ler1):

                ProcessoCelular.processo_entrada[vai[0]-1][lein1] = ProcessoCelular.pico_40

        print("entrada: ",ProcessoCelular.processo_entrada)

    