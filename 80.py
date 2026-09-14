class ProdutoInvalidoError(Exception):
    pass


class ValorInvalidoError(Exception):
    pass


class QuantidadeInvalidaError(Exception):
    pass


def registrar_venda(produto, preco, quantidade):
    if produto.strip() == "":
        raise ProdutoInvalidoError("O nome do produto não pode ser vazio")

    if preco <= 0:
        raise ValorInvalidoError("O preço deve ser maior que zero")

    if not isinstance(quantidade, int) or quantidade <= 0:
        raise QuantidadeInvalidaError("A quantidade deve ser um número inteiro positivo")

    total = preco * quantidade

    return {
        "produto": produto,
        "preco": preco,
        "quantidade": quantidade,
        "total": total
    }


def gerar_relatorio(vendas):
    faturamento = 0
    quantidades = {}

    for venda in vendas:
        faturamento = faturamento + venda["total"]
        produto = venda["produto"]

        if produto in quantidades:
            quantidades[produto] = quantidades[produto] + venda["quantidade"]
        else:
            quantidades[produto] = venda["quantidade"]

    produto_mais_vendido = max(quantidades, key=quantidades.get)
    ticket_medio = faturamento / len(vendas)

    print("Quantidade total de vendas:", len(vendas))
    print("Produto mais vendido:", produto_mais_vendido)
    print("Faturamento total: R$", faturamento)
    print("Ticket médio: R$", ticket_medio)


def registrar_erro(mensagem):
    try:
        with open("log_erros.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(mensagem + "\n")
    except OSError as erro:
        print("Não foi possível registrar o erro no arquivo:", erro)


def salvar_venda(venda):
    try:
        with open("vendas.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(
                venda["produto"] + ";" +
                str(venda["preco"]) + ";" +
                str(venda["quantidade"]) + ";" +
                str(venda["total"]) + "\n"
            )
    except OSError as erro:
        print("Não foi possível gravar a venda no arquivo:", erro)


vendas = []

while True:
    produto = input("Digite o nome do produto ou 'fim' para encerrar: ")

    if produto.lower() == "fim":
        break

    try:
        preco = float(input("Digite o preço unitário: "))
        quantidade = int(input("Digite a quantidade vendida: "))
        venda = registrar_venda(produto, preco, quantidade)
    except ValueError:
        mensagem = "Preço ou quantidade informados em formato inválido"
        print(mensagem)
        registrar_erro(mensagem)
    except (ProdutoInvalidoError, ValorInvalidoError, QuantidadeInvalidaError) as erro:
        print("Erro:", erro)
        registrar_erro(str(erro))
    else:
        vendas.append(venda)
        salvar_venda(venda)
        print("Venda registrada com sucesso")
    finally:
        print("Processamento da venda finalizado")

if len(vendas) > 0:
    gerar_relatorio(vendas)
else:
    print("Nenhuma venda válida foi registrada")
