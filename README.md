# Lanzamiento-de-dardos
Aplicación gráfica interactiva que simula lanzamientos de dardos en un tablero circular, mostrando su ubicación exacta. Además, determina probabilidad de acertar cada área de la diana

## Estructura del código

Iniciamos importando las librerías necesarias para nuestor programa
- `from math import pi`: Importa la constante `pi` del módulo `math`. Será utilizada para calcular áreas más adelante.
- `from random import uniform`: Importa la función `uniform` del módulo `random`. Esta función se utiliza para generar números aleatorios uniformemente distribuidos en un rango.
- `from tkinter import Tk, Canvas, Button, Label`: Importa las clases `Tk`, `Canvas`, `Button` y `Label` del módulo `tkinter`, que se utilizan para crear la interfaz gráfica.

Procedemos a definir una función llamada `areaD` que toma un argumento `x`, que representa el diámetro de un círculo. Esta función calcula y devuelve el área del círculo utilizando la fórmula del área de un círculo: πr^2.
```
def areaD(x)
```
Luego se define una función `def lanzar_dardo()` que se ejecutará cuando se haga clic en el botón "Lanzar dardo". Esta función realiza las siguientes acciones:
- Genera coordenadas `x` e `y` aleatorias dentro del tablero circular.
- Dibuja un punto rojo en el lienzo para representar el dardo lanzado.
- Calcula la distancia del punto al centro del tablero.
- Determina el resultado del lanzamiento (Centro, Blanco, Negro o Fuera) según la distancia.
- Muestra el resultado en una etiqueta en la ventana.

Un bucle `while` solicita al usuario ingresar el diámetro del tablero (`dT`) y asegura que el valor sea mayor que cero.
Otro bucle `while` solicita al usuario ingresar el diámetro del centro (`dC`) y asegura que el valor sea mayor que cero y menor que el diámetro del tablero (`dT`).
```
while True:
    dC = float(input("Ingrese el diámetro del centro:"))
    if(dC > 0 and dC < dT):
        break 
    print("El diámetro del centro debe ser mayor a 0 y menor al diámetro del tablero")
```
Se Procede a calcular las probabilidades de cada zona del tablero: la probabilidad de que el dardo caiga en el centro (`pC`) y la probabilidad de que caiga en la parte blanca o negra del tablero (`pBN`).
```
pC = 100 * areaD(dC) / areaD(dT)
pBN = (100 - pC) / 2
```
Muestra las probabilidades calculadas en la consola.
```
print("Asumiendo que todos los tiros son puntos aleatorios dentro del tablero:")
print("La probabilidad de que el dardo dé en el centro es de " + str(pC) + "%")
print("La probabilidad de que el dardo dé en la parte blanca del tablero es de: " + str(pBN) + "%. Lo mismo para la parte negra del tablero")
```
Crea una ventana Tkinter (`ventana`) con un título.
```
ventana = Tk()
ventana.title("Tiro de dardos")
```
Crea un lienzo (`canvas`) en la ventana para dibujar eltablero y los dardos
```
canvas = Canvas(ventana, width=300, height=300)
canvas.pack()
```
Dibuja el círculo exterior del tablero en negro.
```
canvas.create_oval(0, 0, 300, 300, fill="black")
```
Dibuja el círculo interior del tablero con dos colores alternados (blanco y blanco)
```
canvas.create_arc(150-dT/2, 150-dT/2, 150+dT/2, 150+dT/2, start=45, extent=180, fill="white")
canvas.create_arc(150-dT/2, 150-dT/2, 150+dT/2, 150+dT/2, start=225, extent=180, fill="white")
```
Dibuja el círculo central del tablero en rojo
```
canvas.create_oval(150-dC/2, 150-dC/2, 150+dC/2, 150+dC/2, fill="red")
```
Crea un botón llamado "Lanzar dardo" en la ventana que, cuando se presiona, llama a la función `lanzar_dardo`.
```
boton = Button(ventana, text="Lanzar dardo", command=lanzar_dardo)
boton.pack()
```
Crea una etiqueta en la ventana para mostrar el resultado del lanzamiento
```
etiqueta = Label(ventana, text="Resultado: ")
etiqueta.pack()
```
Finalmente se inicia el bucle principal de la ventana, lo que permite que la aplicación se ejecute y responda a las interacciones del usuario.
```
ventana.mainloop()
```



