import db_manager
from jogador import Jogador

db = db_manager.DBManager("tictactoe.db")

# jogador = Jogador(usuario="eduardo",
#                   cpf="12123232",
#                   email="eduardo@gmail.com",
#                   senha="123456789"
#                   )

# if db.cadastro(jogador):
#     print("Cadastro realizado com sucesso!")

# jogador = db.login("luarde", "123456")
# jogador.partidas += 1
# jogador.vitorias += 1

# if db.update(jogador):
#     print("update 1 realizado com sucesso.")

jogador2 = db.login("eduardo", "123456789")

jogador2.partidas += 1
jogador2.empates  += 1

if db.update(jogador2):
    print("update 2 realizado com sucesso.")

db.disconnect()
