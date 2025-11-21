#1. Заполните экран треугольниками
import tkinter as tk

window = tk.Tk()
canvas_width = 600
canvas_height = 800
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

size = 60  # сторона
for y in range(0, canvas_height, size):
    for x in range(0, canvas_width, size):
        canvas.create_polygon(
            x, y,
            x + size, y,
            x + size // 2, y + size,
            outline='black', fill=''
        )

# теперь цветные треугольники
import random

window = tk.Tk()
canvas_width = 600
canvas_height = 800
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

size = 60
for y in range(0, canvas_height, size):
    for x in range(0, canvas_width, size):
        color = random_color()
        canvas.create_polygon(
            x, y,
            x + size, y,
            x + size // 2, y + size,
            outline='black', fill=color
        )



#2. Движущийся треугольник
import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=200)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)

# Вправо
for x in range(60):
    canvas.move(1, 5, 0)
    tk.update()
    time.sleep(0.05)

# Вниз
for x in range(20):
    canvas.move(1, 0, 5)
    tk.update()
    time.sleep(0.05)

# Влево
for x in range(60):
    canvas.move(1, -5, 0)
    tk.update()
    time.sleep(0.05)

# Вверх
for x in range(20):
    canvas.move(1, 0, -5)
    tk.update()
    time.sleep(0.05)

#3. Движущаяся фотография

# Укажите путь к вашей фотографии
filename = "./data/cat.jpg"

from tkinter import Tk, Canvas
from PIL import Image, ImageTk
import time

root = Tk()
canvas = Canvas(root, width=1000, height=800)
canvas.pack()

img = Image.open(filename)
photo = ImageTk.PhotoImage(img)

# Разместим фото на холсте
image_id = canvas.create_image(50, 50, anchor='nw', image=photo)

# Движение вправо
for _ in range(60):
    canvas.move(image_id, 5, 0)
    root.update()
    time.sleep(0.02)

# Движение вниз
for _ in range(30):
    canvas.move(image_id, 0, 5)
    root.update()
    time.sleep(0.02)

# Движение влево
for _ in range(60):
    canvas.move(image_id, -5, 0)
    root.update()
    time.sleep(0.02)

# Движение вверх
for _ in range(30):
    canvas.move(image_id, 0, -5)
    root.update()
    time.sleep(0.02)

root.mainloop()


