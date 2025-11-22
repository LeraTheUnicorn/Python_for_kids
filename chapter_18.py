from tkinter import *
import time


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Человечек спешит к выходу")
        self.tk.resizable(0, 0)
        self.tk.geometry("1000x1000")
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=1000, height=1000, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 1000
        self.canvas_width = 1000
        self.bg = PhotoImage(file="./data/stickman/background.gif")
        w = self.bg.width()
        h = self.bg.height()
        for x in range(0, 10):
            for y in range(0, 10):
                self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')
        self.sprites = []
        self.running = True

    def mainloop(self):
        self.game_loop()
        self.tk.mainloop()

    def game_loop(self):
        if self.running:
            for sprite in self.sprites:
                sprite.move()
            self.tk.after(10, self.game_loop)


class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @staticmethod
    def within_x(co1, co2):
        if (co1.x1 > co2.x1 and co1.x1 < co2.x2) or (co1.x2 > co2.x1 and co1.x2 < co2.x2) or (
                co2.x1 > co1.x1 and co2.x1 < co1.x2) or (co2.x2 > co1.x1 and co2.x2 < co1.x2):
            return True
        else:
            return False

    @staticmethod
    def within_y(co1, co2):
        if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
                or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
                or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
                or (co2.y2 > co1.y1 and co2.y2 < co1.y2):
            return True
        else:
            return False

    @staticmethod
    def collided_left(co1, co2):
        if Coords.within_y(co1, co2):
            if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
                return True
            return False

    @staticmethod
    def collided_right(co1, co2):
        if Coords.within_y(co1, co2):
            if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
                return True
        return False

    @staticmethod
    def collided_top(co1, co2):
        if Coords.within_x(co1, co2):
            if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
                return True
        return False

    @staticmethod
    def collided_bottom(y, co1, co2):
        if Coords.within_x(co1, co2):
            y_calc = co1.y2 + y
            if y_calc >= co2.y1 and y_calc <= co2.y2:
                return True
        return False


class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None

    def move(self):
        pass

    def coords(self):
        return self.coordinates


class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x + width, y + height)


class StickFigureSprite(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game)
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

        self.image = game.canvas.create_image(0, 900, image=self.images_left[0], anchor='nw')
        self.x = 0
        self.y = 0
        self.current_image = 0
        self.current_image_add = 1
        self.last_time = time.time()
        self.coordinates = Coords()
        self.on_ground = False
        self.won = False
        game.tk.bind_all('<KeyPress-Left>', self.turn_left)
        game.tk.bind_all('<KeyPress-Right>', self.turn_right)
        game.tk.bind_all('<KeyRelease-Left>', self.stop_left)
        game.tk.bind_all('<KeyRelease-Right>', self.stop_right)
        game.tk.bind_all('<space>', self.jump)

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
        if self.on_ground:
            self.y = -7

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
                self.game.canvas.itemconfig(self.image, image=self.images_left[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.images_left[self.current_image])
        elif self.x > 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.images_right[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.images_right[self.current_image])

    def coords(self):
        xy = self.game.canvas.coords(self.image)
        if self.coordinates is None:
            self.coordinates = Coords()
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30
        return self.coordinates

    def move(self):
        self.animate()
        co = self.coords()
        left = True
        right = True
        top = True
        bottom = True
        falling = True
        self.on_ground = False
        if self.y > 0 and co.y2 >= self.game.canvas_height:
            self.y = 0
            bottom = False
            self.on_ground = True
        elif self.y < 0 and co.y1 <= 0:
            self.y = 0
            top = False
        if self.x > 0 and co.x2 >= self.game.canvas_width:
            self.x = 0
            right = False
        elif self.x < 0 and co.x1 <= 0:
            self.x = 0
            left = False
        for sprite in self.game.sprites:
            if sprite == self:
                continue
            sprite_co = sprite.coords()
            if top and self.y < 0 and Coords.collided_top(co, sprite_co):
                self.y = -self.y
                top = False
            if bottom and self.y > 0 and Coords.collided_bottom(self.y, co, sprite_co):
                self.y = sprite_co.y1 - co.y2
                if self.y < 0:
                    self.y = 0
                bottom = False
                top = False
                self.on_ground = True
            if bottom and falling and self.y == 0 and co.y2 < self.game.canvas_height and Coords.collided_bottom(1, co, sprite_co):
                falling = False
                self.on_ground = True
            if left and self.x < 0 and Coords.collided_left(co, sprite_co):
                self.x = 0
                left = False
                if sprite.endgame:
                    if not self.won:
                        sprite.game.canvas.itemconfig(sprite.image, image=sprite.photo_image2)
                        self.game.canvas.itemconfig(self.image, state='hidden')
                        self.game.canvas.create_text(250, 250, text="победа", font=("Arial", 50), fill="red")
                        self.won = True
                    self.game.running = False
            if right and self.x > 0 and Coords.collided_right(co, sprite_co):
                self.x = 0
                right = False
                if sprite.endgame:
                    if not self.won:
                        sprite.game.canvas.itemconfig(sprite.image, image=sprite.photo_image2)
                        self.game.canvas.itemconfig(self.image, state='hidden')
                        self.game.canvas.create_text(250, 250, text="победа", font=("Arial", 50), fill="red")
                        self.won = True
                    self.game.running = False
            if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
                self.y = 4
        self.game.canvas.move(self.image, self.x, self.y)
        # Гравитация
        self.y += 0.08
        xy = self.game.canvas.coords(self.image)
        if xy[1] >= 900:
            self.y = 0
            self.on_ground = True
        # Ограничение границ
        if xy[0] < 0:
            self.game.canvas.coords(self.image, 0, xy[1])
            self.x = 0
        elif xy[0] > self.game.canvas_width - 27:
            self.game.canvas.coords(self.image, self.game.canvas_width - 27, xy[1])
            self.x = 0
        if xy[1] < 0:
            self.game.canvas.coords(self.image, xy[0], 0)
            self.y = 0
        elif xy[1] > 770:
            self.game.canvas.coords(self.image, xy[0], 770)
            self.y = 0
            self.on_ground = True


class DoorSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.photo_image2 = PhotoImage(file="./data/stickman/door2.gif")
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x + (width / 2), y + height)
        self.endgame = True


g = Game()
platform1 = PlatformSprite(g, PhotoImage(file="./data/stickman/platform1.gif"), 0, 150, 100, 20)
platform2 = PlatformSprite(g, PhotoImage(file="./data/stickman/platform1.gif"), 550, 400, 100, 20)
platform3 = PlatformSprite(g, PhotoImage(file="./data/stickman/platform1.gif"), 50, 650, 100, 10)
platform4 = PlatformSprite(g, PhotoImage(file="./data/stickman/platform1.gif"), 550, 850, 100, 10)
g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
door = DoorSprite(g, PhotoImage(file="./data/stickman/door1.gif"), 45, 30, 40, 35)
g.sprites.append(door)
player = StickFigureSprite(g)
g.sprites.append(player)
g.mainloop()
