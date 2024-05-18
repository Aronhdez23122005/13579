from turtle import *

# Función para dibujar una flor redonda
def draw_flower(x, y):
    penup()
    goto(x, y)
    pendown()
    color("yellow", "yellow")  # Contorno amarillo, relleno púrpura
    begin_fill()
    for _ in range(9):  # Ajustar para 9 pétalos
        circle(20, 180)  # Dibuja un semicírculo (180 grados)
        left(140)  # Ajusta el ángulo para el siguiente pétalo
    end_fill()

# Configuración inicial
bgcolor("black")
color("red")
title("Heart")

# Dibujo del corazón
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

# Dibujo del mensaje
penup()
goto(0, -70)
pendown()
color("red")
write("Buenos Dias Flaka hermosa", align="center", font=("Brush Script MT", 30, "normal"))

# Dibujo de las flores

draw_flower(200, -20)   # Flor a la derecha del corazón

# Finalización
hideturtle()
done()


