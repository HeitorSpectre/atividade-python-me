import traceback


def processar_dados(dados):
    for dado in dados:
        try:
            numero = float(dado)
            print("Valor processado:", numero)
        except (TypeError, ValueError):
            print("Não foi possível processar:", dado)
            traceback.print_exc()


dados = [10, "20", "abc", None, 5.5, "30.2"]
processar_dados(dados)
