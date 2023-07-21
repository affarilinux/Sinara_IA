
from BANCO_DADOS.estrutura_base import EstruturaBase

class ListaEntrada(EstruturaBase):

    def neuronio_tabela(self):
        
        self.cursorsq.execute(
            """CREATE TABLE if not exists CAMADA_ENTRADA(
            ID_ENTRADA INTEGER PRIMARY KEY AUTOINCREMENT,
            NEURONIO TEXT
            )"""
        )

        self.commit_banco()

    def count_return(self):

        self.criar_banco()
        self.ativar_banco()

        self.neuronio_tabela() ## inicio verificacao

        self.cursorsq.execute(
            """SELECT COUNT(ID_ENTRADA) FROM CAMADA_ENTRADA """) 
                    
        coun = self.cursorsq.fetchone()
        
        self.commit_banco()
        self.sair_banco()
        
        return coun[0]    
    
    def camada_inserir(self,NEU):

        self.criar_banco()
        self.ativar_banco()

        self.cursorsq.execute(
            """INSERT INTO CAMADA_ENTRADA(NEURONIO) 
            VALUES(?)""",(NEU,))
    
        self.commit_banco()
        self.sair_banco()

    def maxx_return_camada(self):

        self.criar_banco()
        self.ativar_banco()

        self.cursorsq.execute(
            """SELECT MAX(ID_ENTRADA) FROM CAMADA_ENTRADA """) 
                    
        MAX = self.cursorsq.fetchone()
        
        self.commit_banco()
        self.sair_banco()
        
        return MAX[0]
    
    def camada_select(self,id_):
       
        self.criar_banco()
        self.ativar_banco()

        self.cursorsq.execute(
            """SELECT NEURONIO FROM CAMADA_ENTRADA
            WHERE  ID_ENTRADA = ?""",(id_,))
        
        id_sel = self.cursorsq.fetchall()
        
        self.commit_banco()
        self.sair_banco()
        
        return id_sel