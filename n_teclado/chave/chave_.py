from n_teclado.processo_celular import ProcessoCelular
from n_teclado.chave.chave_entrada import ChaveEntrada

class ChaveInicial:
    
    def iniciar_entrada(self):
        
        ce = ChaveEntrada()
        ce.init_rede_entrada()

    