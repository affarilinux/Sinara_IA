from n_teclado.processo_celular import ProcessoCelular
from n_teclado.chave.chave_entrada import ChaveEntrada

class ChaveInicial:
    
    def __init__(self) -> None:
        
        
        pc = len(ProcessoCelular.processo_entrada)

        if pc == 0:

            ce = ChaveEntrada()
            ce.init_rede_entrada()

    