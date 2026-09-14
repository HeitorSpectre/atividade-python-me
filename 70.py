def buscar_permissao(perfil, chave, indice):
    try:
        return perfil[chave][indice]
    except (KeyError, IndexError):
        return "acesso_restrito"


perfil = {
    "administrador": ["leitura", "escrita", "exclusão"],
    "usuario": ["leitura"]
}

chave = input("Digite o perfil: ")
indice = int(input("Digite o índice da permissão: "))

print(buscar_permissao(perfil, chave, indice))
