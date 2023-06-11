import sqlite3

class EstruturaBase:

    def criar_banco(self):
        self.bancovar = sqlite3.connect('BANCO_DADOS/neuronio.db')
        
    def ativar_banco(self):
            
            self.cursorsq = self.bancovar.cursor()

    def commit_banco(self):
            self.bancovar.commit()

    def sair_banco(self):
            self.cursorsq.close()
            self.bancovar.close()