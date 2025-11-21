# 1. Жирафий танец
import turtle


class Giraffes:
    def left_foot_forward(self):
        print('левая нога впереди')

    def left_foot_back(self):
        print('левая нога сзади')

    def right_foot_forward(self):
        print('правая нога впереди')

    def right_foot_back(self):
        print('правая нога сзади')

    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()


reginald = Giraffes()
reginald.dance()

# 2. Черепашьи вилы

# Верхняя стрелка
arrow_1 = turtle.Pen()
arrow_1.goto(200, 0)
arrow_1.left(90)
arrow_1.forward(50)
arrow_1.right(90)
arrow_1.forward(50)

# Верхняя стрелка 2
arrow_2 = turtle.Pen()
arrow_2.goto(150, 0)
arrow_2.left(90)
arrow_2.forward(100)
arrow_2.right(90)
arrow_2.forward(100)

# Нижняя стрелка
arrow_3 = turtle.Pen()
arrow_3.goto(200, 0)
arrow_3.right(90)
arrow_3.forward(50)
arrow_3.left(90)
arrow_3.forward(50)

# Нижняя стрелка 2
arrow_4 = turtle.Pen()
arrow_4.goto(150, 0)
arrow_4.right(90)
arrow_4.forward(100)
arrow_4.left(90)
arrow_4.forward(100)

turtle.done()
