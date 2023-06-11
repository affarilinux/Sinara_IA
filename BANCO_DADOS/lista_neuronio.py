from BANCO_DADOS.estrutura_base import EstruturaBase

class ListaNeuronio_db(EstruturaBase):

    def neuronio_tabela(self):

        self.criar_banco()
        self.ativar_banco()
        
        self.cursorsq.execute(
            """CREATE TABLE if not exists NEURONIO(
            ID_NEURONIO INTEGER PRIMARY KEY AUTOINCREMENT,
            NEURONIO TEXT
            )""")
        
        self.commit_banco()
        self.sair_banco()

    