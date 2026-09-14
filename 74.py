produtos = {
    1: "Teclado",
    2: "Mouse",
    3: "Monitor"
}


def buscar_produto(produto_id):
    try:
        produto = produtos[produto_id]
        return {"produto": produto}, 200
    except KeyError:
        return {"erro": "Produto não encontrado"}, 404
    except Exception:
        return {"erro": "Erro interno do servidor"}, 500


produto_id = int(input("Digite o ID do produto: "))
resposta, status = buscar_produto(produto_id)

print(resposta)
print("HTTP Status:", status)
