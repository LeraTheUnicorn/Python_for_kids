# 1. Рисуем восьмиугольник
import turtle


def draw_octagon(side_length):
    t = turtle.Pen()
    for _ in range(8):
        t.forward(side_length)
        t.left(45)


# Пример вызова:
draw_octagon(60)

turtle.resetscreen()


# 2. Заполненный восьмиугольник

def draw_filled_octagon(side_length):
    t = turtle.Pen()
    t.color('black', 'yellow')  # линии черные, заливка желтая
    t.begin_fill()
    for _ in range(8):
        t.forward(side_length)
        t.left(45)
    t.end_fill()


# Пример вызова:
draw_filled_octagon(60)

turtle.resetscreen()


# 3. Еще одна функция для рисования звезд

def draw_star(size, points):
    angle = 180 - 180 / points
    t = turtle.Pen()
    for _ in range(points):
        t.forward(size)
        t.right(angle)


# Пример вызова:
draw_star(120, 7)  # звезда

turtle.done()
