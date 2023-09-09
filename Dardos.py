from math import pi
from random import uniform
from tkinter import Tk, Canvas, Button, Label

# Función para calcular el área de un círculo dado su diámetro
def areaD(x):
    r = x/2
    a = r*r*pi
    return a

# Función para lanzar un dardo aleatorio dentro del tablero
def lanzar_dardo():
    # Generar una coordenada aleatoria dentro del tablero
    x = uniform(-dT/2, dT/2)
    y = uniform(-dT/2, dT/2)
    # Dibujar un punto rojo en el lugar del dardo
    canvas.create_oval(x+150-2, y+150-2, x+150+2, y+150+2, fill="red")
    # Calcular la distancia al centro del tablero
    distancia = (x*2 + y*2)**0.5
    # Determinar el resultado del lanzamiento según la distancia
    if distancia <= dC/2:
        resultado = "Centro"
    elif distancia <= dT/2:
        if (x > 0 and y > 0) or (x < 0 and y < 0):
            resultado = "Blanco"
        else:
            resultado = "Negro"
    else:
        resultado = "Fuera"
    # Mostrar el resultado en la etiqueta
    etiqueta.config(text="Resultado: " + resultado)

# Pedir al usuario el diámetro del tablero
while True:
    dT = float(input("Ingrese el diámetro del tablero:"))
    if dT > 0:
        break
    print("El diámetro del tablero debe ser mayor a 0")

# Pedir al usuario el diámetro del centro
while True:
    dC = float(input("Ingrese el diámetro del centro:"))
    if(dC > 0 and dC < dT):
        break 
    print("El diámetro del centro debe ser mayor a 0 y menor al diámetro del tablero")

# Calcular las probabilidades de cada zona del tablero
pC = 100 * areaD(dC) / areaD(dT)
pBN = (100 - pC) / 2

print("Asumiendo que todos los tiros son puntos aleatorios dentro del tablero:")
print("La probabilidad de que el dardo dé en el centro es de " + str(pC) + "%")
print("La probabilidad de que el dardo dé en la parte blanca del tablero es de: " + str(pBN) + "%. Lo mismo para la parte negra del tablero")

# Crear una ventana con Tkinter
ventana = Tk()
ventana.title("Tiro de dardos")

# Crear un lienzo para dibujar el tablero
canvas = Canvas(ventana, width=300, height=300)
canvas.pack()

# Dibujar el círculo exterior del tablero
canvas.create_oval(0, 0, 300, 300, fill="black")

# Dibujar el círculo interior del tablero con dos colores alternados
canvas.create_arc(150-dT/2, 150-dT/2, 150+dT/2, 150+dT/2, start=45, extent=180, fill="white")
canvas.create_arc(150-dT/2, 150-dT/2, 150+dT/2, 150+dT/2, start=225, extent=180, fill="white")

# Dibujar el círculo central del tablero
canvas.create_oval(150-dC/2, 150-dC/2, 150+dC/2, 150+dC/2, fill="red")

# Crear un botón para lanzar un dardo
boton = Button(ventana, text="Lanzar dardo", command=lanzar_dardo)
boton.pack()

# Crear una etiqueta para mostrar el resultado del lanzamiento
etiqueta = Label(ventana, text="Resultado: ")
etiqueta.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
