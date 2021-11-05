# Adivina_el_n-mero

Mi direccion de GitHub para este repositorio es la siguiente: [GitHUb](https://github.com/AnaLopezP/Adivina_el_numero.git)
https://github.com/AnaLopezP/Adivina_el_numero.git

Hemos resuelto un juego de adivinar números, en el que la máquina elige un número aleatorio entero entre 0 y 99 y mediante pistas de frío o caliente, el usuario va a adivinar tal número.
El diagrama de flujo que tenemos en nuestro código es el siguiente:

![diagrama de flujo adivine el número](/AnaLopezP/Adivina_el_numero/Adivina_el_número_flujo.jpg)

```import random
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
