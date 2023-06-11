from universal.estruturaneuroniobase import NeuronioBase
from n_teclado.listas_neuronio import listaEntrada

class NeuroSaida:

    def __init__(self,entrada_peso):
        pis = NeuronioBase()
        lista_sai_a = listaEntrada()

        saida = [
            #neuronio a
            entrada_peso[0] * lista_sai_a.lista_nos_entrada[0],
            #neuronio c
            entrada_peso[1] * lista_sai_a.lista_nos_entrada[1],
            #s
            entrada_peso[2] * lista_sai_a.lista_nos_entrada[2]
            ]
        saida_var = 0

        print(saida)
        ativo = True
        
        while ativo:
        
            if saida[saida_var] >= pis.limiardisparo_m55:

                self.sit(saida_var)

                ativo = False

            saida_var = saida_var +1
            
    def sit(self,at):

        if at == 0:

            self.pal("a")

        elif at == 1:

            self.pal("c")

        elif at == 2:

            self.pal("s")

    def pal(self,adf):
        
        print("resultado: {}".format(adf))

