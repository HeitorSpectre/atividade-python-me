def contar_caractere(texto, caractere):
    return texto.count(caractere)


texto = input("Digite uma frase: ")
caractere = input("Digite um caractere: ")

print("O caractere aparece", contar_caractere(texto, caractere), "vezes")
