import random
numero = random.randint(0,100)
print(numero)
print("Intente con un número entero.")
intento = input()
while str(intento) != str(numero):
    if str(intento) > str(99):
        print("El número está entre 0 y 99. Elige otro.")
    else:
        if str(intento) > str(numero):
            print("Te has pasado. El numero está entre 0 y " + str(intento) + ".")
        else:
            print("Te has quedado corto. El numero está entre " + str(intento) + " y 99.")
    intento = input()
if str(intento) == str(numero):
     print("¡Felicidades, has acertado!")