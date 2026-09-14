import random


def conectar_api():
    if random.choice([True, False]):
        raise ConnectionError("Falha na conexão")

    return "Conexão realizada"


def conexao_resiliente():
    for tentativa in range(1, 4):
        try:
            resultado = conectar_api()
            print(resultado)
            return
        except ConnectionError as erro:
            print("Tentativa", tentativa, "falhou:", erro)

    print("Não foi possível conectar após 3 tentativas")


conexao_resiliente()
