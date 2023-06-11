
class Criartabela:

    def __init__(self) -> None:
        
        self.cursorsq.execute(
            """CREATE TABLE if not exists RAM(
            ID_RAM INTEGER PRIMARY KEY AUTOINCREMENT,
            RAM_MINIMO INT,
            RAM_MAXIMO INT,
            RAM_APRESENTAR INT
            )""")