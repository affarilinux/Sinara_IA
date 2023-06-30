class NeuronioBase:

    def __init__(self) -> None:
    
        self.pico_40 = 40

        self.limiardisparo_m55 = -55

        self.potencialrepouso_m70 = -70

    def cal_pontencial(self,QT_sinapse):
        
        divisa = ((
            self.pico_40 - (self.potencialrepouso_m70) 
            ) / QT_sinapse)
        
        divisa2 =  round(self.potencialrepouso_m70 + divisa, 3 )
        
        return divisa2
    
    def cal_lista_sistema(self,lista_acesso):
        
        somar = 0
        for list_ in range(0,len(lista_acesso)):

            somar = somar + lista_acesso[list_]
            
        return somar
    
    def loop_camada_neuronio(self,lista_individual,cal_potencial,neuronio):

        for list_individual_ in range(0,len(lista_individual)):

            if lista_individual[list_individual_] != 0:

                llist = lista_individual[list_individual_] * cal_potencial

                if llist >= self.limiardisparo_m55:

                    neuronio[list_individual_] = self.pico_40

        return neuronio

    

    
        
