from BANCO_DADOS.estrutura_base import EstruturaBase

class Teclas(EstruturaBase):

    def teclas_tabelas(self):
        
        self.criar_banco()
        self.ativar_banco()

        self.cursorsq.execute(
            """CREATE TABLE if not exists LISTA_TECLAS(
            ID_TECLAS INTEGER PRIMARY KEY AUTOINCREMENT,
            TECLAS TEXT
            )""")
        
        self.commit_banco()
        self.sair_banco()
    
    def count_return_teclas(self):

        self.criar_banco()
        self.ativar_banco()

        self.cursorsq.execute(
            """SELECT COUNT(ID_TECLAS) FROM LISTA_TECLAS """) 
                    
        coun = self.cursorsq.fetchone()
        
        self.commit_banco()
        self.sair_banco()
        
        return coun[0]    
    
    def teclas_inserir(self,letras):

        self.teclas_tabelas()

        self.criar_banco()
        self.ativar_banco()
        
        self.cursorsq.execute(
            """INSERT INTO LISTA_TECLAS(TECLAS) VALUES(?)""",
            (letras,))
        
        self.commit_banco()

        self.sair_banco()

        #**********************************

        self.criar_banco()
        self.ativar_banco()

        self.cursorsq.execute(
            """SELECT TECLAS FROM LISTA_TECLAS WHERE  TECLAS = ?""",
            (letras,))
        
        cell = self.cursorsq.fetchone()

        if cell == None:

            print("caractere não inserido")

        elif cell != None:

            print("caractere inserido no banco")

        self.sair_banco()

    def teclas_return(self,ret_letras):
    
        self.teclas_tabelas()
        
        self.criar_banco()
        self.ativar_banco()

        self.cursorsq.execute(
            """SELECT ID_TECLAS FROM LISTA_TECLAS WHERE  TECLAS = ?""",
            (ret_letras,))
        
        sell = self.cursorsq.fetchone()
        
        self.commit_banco()
        self.sair_banco()
        
        return sell
    
    