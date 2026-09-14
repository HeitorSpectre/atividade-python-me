def inverter_texto(texto):
    return texto[::-1]


textos = (
    "python2023",
    "0203programacao2023",
    "luz azul",
    "arara rara",
    "anotaram a data da maratona"
)

for texto in textos:
    print(inverter_texto(texto))
