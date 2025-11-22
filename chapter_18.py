from tkinter import *
import time

class StickFigureSprite:
    def __init__(self, tk, canvas):
        self.tk = tk
        self.canvas = canvas
        self.images_left = [
            PhotoImage(file="./data/stickman/man04.gif"),
            PhotoImage(file="./data/stickman/man05.gif"),
            PhotoImage(file="./data/stickman/man06.gif")
        ]
        self.images_right = [
            PhotoImage(file="./data/stickman/man01.gif"),
            PhotoImage(file="./data/stickman/man02.gif"),
            PhotoImage(file="./data/stickman/man03.gif")
        ]

        self.image = canvas.create_image(200, 470, image=self.images_left[0], anchor='nw')
        self.x = 0
        self.y = 0
        self.current_image = 0
        self.current_image_add = 1
        self.last_time = time.time()
        tk.bind('<KeyPress-Left>', self.turn_left)
        tk.bind('<KeyPress-Right>', self.turn_right)
        tk.bind('<KeyRelease-Left>', self.stop_left)
        tk.bind('<KeyRelease-Right>', self.stop_right)
        tk.bind('<space>', self.jump)
        self.game_loop()

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def stop_left(self, evt):
        if self.x < 0:
            self.x = 0

    def stop_right(self, evt):
        if self.x > 0:
            self.x = 0

    def jump(self, evt):
        if self.y == 0:
            self.y = -3

    def animate(self):
        if self.x != 0 and self.y == 0:
            if time.time() - self.last_time > 0.1:
                self.last_time = time.time()
                self.current_image += self.current_image_add
                if self.current_image >= 2:
                    self.current_image_add = -1
                if self.current_image <= 0:
                    self.current_image_add = 1
        if self.x < 0:
            if self.y != 0:
                self.canvas.itemconfig(self.image, image=self.images_left[2])
            else:
                self.canvas.itemconfig(self.image, image=self.images_left[self.current_image])
        elif self.x > 0:
            if self.y != 0:
                self.canvas.itemconfig(self.image, image=self.images_right[2])
            else:
                self.canvas.itemconfig(self.image, image=self.images_right[self.current_image])

    def move(self):
        self.animate()
        # Простое движение без столкновений
        xy = self.canvas.coords(self.image)
        if self.x < 0 and xy[0] > 0:
            pass  # можно двигаться
        elif self.x > 0 and xy[0] < 500 - 27:
            pass
        else:
            self.x = 0
        if self.y < 0 and xy[1] > 0:
            pass
        elif self.y > 0 and xy[1] < 500 - 30:
            pass
        else:
            self.y = 0
        self.canvas.move(self.image, self.x, self.y)
        # Гравитация
        self.y += 0.08
        xy = self.canvas.coords(self.image)
        if xy[1] >= 470:
            self.y = 0

    def game_loop(self):
        self.move()
        self.tk.after(10, self.game_loop)


tk = Tk()
tk.title("Движение персонажа")
tk.resizable(0, 0)
canvas = Canvas(tk, width=500, height=500, highlightthickness=0)
canvas.pack()
tk.update()

player = StickFigureSprite(tk, canvas)
tk.mainloop()
