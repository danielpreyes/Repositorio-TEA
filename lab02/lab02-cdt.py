# Tendencias e Innovacion en Tecnologia Agricola (TEA)
minutos = input("minutos jugados?")
valorPorMinuto = input("valor por minuto?")

# se utiliza la conversacion de tipo a int
# sino se hace la conversion existira error porque trata de multiplicar strings
# calculando el valor total de las minutos jugadas
total = int(minutos) * int(valorPorMinuto)
print ("total= "+ str(total))
