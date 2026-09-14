def fahrenheit_para_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


temperatura = float(input("Digite a temperatura em Fahrenheit: "))
print("Temperatura em Celsius:", fahrenheit_para_celsius(temperatura))
