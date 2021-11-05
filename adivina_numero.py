import random
numero = random.randint(0,100)
print(numero)
print("Intente con un número entero.")
intento = int(input())
while intento != numero:
    if intento > 99:
        print("El número está entre 0 y 99. Elige otro.")
    else:
        if intento > numero:
            print("Te has pasado.")
        else:
            print("Te has quedado corto.")
    intento = int(input())
if intento == numero:
     print("¡Felicidades, has acertado!")