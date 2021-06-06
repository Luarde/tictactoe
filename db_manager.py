import sqlite3 as connector
from jogador import Jogador


class DBManager:
    # Criação do cursor e recebimento do database como parâmetro
    
    def __init__(self, database):
        self.connector = None
        self.cursor = None
        self.database = database

        self.connect()

    # Conexão ao banco e ajustes em caso de erro de conexão
    def connect(self):
        try:
            self.connector = connector.connect(self.database)
            self.cursor = self.connector.cursor()
        except (connector.IntegrityError, connector.DatabaseError,
                connector.ProgrammingError
                ) as Error:
            print("Falha ao se conectar", Error)

    # Se a o connector e o cursor retornar None, ele tenta realizar a conexão com banco
    def check_connection(self):
        if self.connector is None or self.cursor is None:
            self.connect()
            
    # Desconectando o database 
    def disconnect(self):
        try:
            self.connector.close()
            self.cursor.close()

            self.connector = None
            self.cursor    = None

        except (connector.IntegrityError, connector.DatabaseError,
                connector.ProgrammingError
                ) as Error:
            print("Falha ao se desconectar", Error)


    # Cadastro de usuário no banco
    def cadastro(self, jogador):
        self.check_connection()

        try:
            # Query para inserção dos parâmetros do arquivo jogador.py dentro do banco.
            query = f"INSERT INTO jogador (usuario, pwd, email, cpf) VALUES ('{jogador.usuario}', '{jogador.senha}', '{jogador.email}', '{jogador.cpf}')"
            # Execução da query com os dados passados
            self.cursor.execute(query)
            # Atualização inserção definitiva dos dados no banco
            self.connector.commit()

        except (connector.IntegrityError, connector.DatabaseError,
                connector.ProgrammingError
                ) as Error:
            print("Erro no Cadastro", Error)
            return False

        return True

    # Logando e validando no banco
    def login(self, usuario, pwd):
        self.check_connection()

        try:
            # Confirmação dos dados passados no main.py onde o usuário passado é igual ao usuário cadastrado no banco
            query = f"SELECT * FROM jogador WHERE usuario = '{usuario}';"
            # Execução da query
            self.cursor.execute(query)
            # Retorno da validação dos dados em uma tupla com os dados informados para comparação e o retorno boolean da conexão
            registro = self.cursor.fetchone()
            # Se o retorno anterior não for None, os dados será desempacotado e será construido uma classe jogador
            # com usuario, pwd, email, cpf, partidas, vitorias, derrotas, empates como criada no jogador.py 
            if registro is not None:
                jogador = Jogador(*registro)
                # Se a senha do banco for igual a senha do registro, os dados do jogador são retornados, senão retorna None 
                if jogador.senha == pwd:
                    return jogador

        except (connector.IntegrityError, connector.DatabaseError,
                connector.ProgrammingError
                ) as Error:
            print(Error)
        return None

    # Atualizando os dados do usuário
    def update(self, jogador):
        self.check_connection()
        
        try:
            # Setando os dados onde o usuário é igual ao usuário passado anteriormente
            query = f"UPDATE jogador SET partidas = '{jogador.partidas}', vitorias = '{jogador.vitorias}', derrotas = '{jogador.derrotas}', empates = '{jogador.empates}' WHERE usuario = '{jogador.usuario}'"
            self.cursor.execute(query)
            self.connector.commit()
            
        except (connector.IntegrityError, connector.DatabaseError,
                connector.ProgrammingError
                ) as Error:
            print("Erro no Cadastro", Error)
            return False

        return True
