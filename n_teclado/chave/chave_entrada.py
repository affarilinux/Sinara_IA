from BANCO_DADOS.lista_neuronio_entrada import ListaEntrada

from n_teclado.processo_celular import ProcessoCelular

"""
    criar lista de entrada para inicio do sistema
    """
class ChaveEntrada:

    def __init__(self) -> None:
        
        self.lne = ListaEntrada()

    def init_rede_entrada(self):

        contar = self.lne.count_return()

        if contar == 0:

            self.rede_zero()
        
        else:

            self.rede_tb_neuronio()
            self.rede_inserir()


    def rede_zero(self):

        self.lne.camada_inserir("1")

        self.init_rede_entrada()

    def rede_tb_neuronio(self):
        
        maxi = self.lne.maxx_return_camada()

        self.var_temp = []
       
        #neuronio
        for cam in range(0,maxi): # pega a lista string

            unidade = self.lne.camada_select(cam+1)

            ### pode dar erro na tabela caso tenha apagado algo na lista
            self.var_temp.append(int(unidade[0][0])) 

    def rede_inserir(self):

        lerint = len(self.var_temp)

        var_temp2 = []

        for cam1 in range(0,lerint):

            for cam2 in range(0,self.var_temp[cam1]):

                var_temp2.append(ProcessoCelular.potencialrepouso_m70)

            ProcessoCelular.processo_entrada.append(var_temp2)

            var_temp2 = []     
            
    def calculo_lista(self,var_if):

        while_var = True

        while while_var:

            contar = self.lne.count_return()

            if contar == var_if:

                while_var = False
            
            else:

                ProcessoCelular.processo_entrada = []

                self.rede_zero()