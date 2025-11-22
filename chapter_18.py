from tkinter import *
import time


class Game:
    def __init__(self):
        """
        Инициализирует игру: создает окно Tkinter, холст, загружает фон и подготавливает список спрайтов.
        Параметры: нет.
        """
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
        """
        Запускает главный цикл игры и Tkinter mainloop.
        Параметры: нет.
        """
        self.game_loop()
        self.tk.mainloop()

    def game_loop(self):
        """
        Основной игровой цикл: обновляет спрайты и планирует следующий вызов.
        Параметры: нет.
        """
        if self.running:
            for sprite in self.sprites:
                sprite.move()
        if self.sprites and hasattr(self.sprites[-1], 'animate_win'):
            self.sprites[-1].animate_win()
        self.tk.after(10, self.game_loop)


class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        """
        Инициализирует координаты прямоугольника.
        Параметры: x1, y1 - верхний левый угол; x2, y2 - нижний правый угол.
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @staticmethod
    def within_x(co1, co2):
        """
        Проверяет, пересекаются ли два прямоугольника по оси X.
        Параметры: co1, co2 - объекты Coords.
        Возвращает: True если пересекаются, иначе False.
        """
        if (co1.x1 >= co2.x1 and co1.x1 <= co2.x2) or (co1.x2 >= co2.x1 and co1.x2 <= co2.x2) or (
                co2.x1 >= co1.x1 and co2.x1 <= co1.x2) or (co2.x2 >= co1.x1 and co2.x2 <= co1.x2):
            return True
        else:
            return False

    @staticmethod
    def within_y(co1, co2):
        """
        Проверяет, пересекаются ли два прямоугольника по оси Y.
        Параметры: co1, co2 - объекты Coords.
        Возвращает: True если пересекаются, иначе False.
        """
        if (co1.y1 >= co2.y1 and co1.y1 <= co2.y2) \
                or (co1.y2 >= co2.y1 and co1.y2 <= co2.y2) \
                or (co2.y1 >= co1.y1 and co2.y1 <= co1.y2) \
                or (co2.y2 >= co1.y1 and co2.y2 <= co1.y2):
            return True
        else:
            return False

    @staticmethod
    def collided_left(co1, co2):
        """
        Проверяет столкновение левой стороны co1 с co2.
        Параметры: co1, co2 - объекты Coords.
        Возвращает: True если столкновение, иначе False.
        """
        if co1.x1 <= co2.x2 and co1.x1 >= co2.x1 and Coords.within_y(co1, co2):
            return True
        return False

    @staticmethod
    def collided_right(co1, co2):
        """
        Проверяет столкновение правой стороны co1 с co2.
        Параметры: co1, co2 - объекты Coords.
        Возвращает: True если столкновение, иначе False.
        """
        if co1.x2 >= co2.x1 and co1.x2 <= co2.x2 and Coords.within_y(co1, co2):
            return True
        return False

    @staticmethod
    def collided_top(co1, co2):
        """
        Проверяет столкновение верхней стороны co1 с co2.
        Параметры: co1, co2 - объекты Coords.
        Возвращает: True если столкновение, иначе False.
        """
        if co1.y1 <= co2.y2 and co1.y1 >= co2.y1 and Coords.within_x(co1, co2):
            return True
        return False

    @staticmethod
    def collided_bottom(co1, co2):
        """
        Проверяет столкновение нижней стороны co1 с co2.
        Параметры: co1, co2 - объекты Coords.
        Возвращает: True если столкновение, иначе False.
        """
        if co1.y2 >= co2.y1 and co1.y2 <= co2.y2 and Coords.within_x(co1, co2):
            return True
        return False


class Sprite:
    def __init__(self, game):
        """
        Базовый класс для спрайтов. Инициализирует общие атрибуты.
        Параметры: game - объект Game.
        """
        self.game = game
        self.endgame = False
        self.coordinates = None

    def move(self):
        """
        Метод движения спрайта. Переопределяется в подклассах.
        Параметры: нет.
        """
        pass

    def coords(self):
        """
        Возвращает координаты спрайта.
        Параметры: нет.
        Возвращает: объект Coords.
        """
        return self.coordinates


class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y):
        """
        Инициализирует спрайт платформы: создает изображение 1:1 и координаты на основе реальных размеров изображения.
        Параметры: game - объект Game; photo_image - PhotoImage; x, y - позиция.
        """
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.width = self.photo_image.width()
        self.height = self.photo_image.height()
        self.coordinates = Coords(x, y, x + self.width, y + self.height)


class StickFigureSprite(Sprite):
    def __init__(self, game):
        """
        Инициализирует спрайт человечка: загружает изображения, устанавливает начальную позицию и привязывает клавиши.
        Параметры: game - объект Game.
        """
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

        self.image = game.canvas.create_image(50, 1000, image=self.images_left[0], anchor='nw')
        self.width = self.images_left[0].width()
        self.height = self.images_left[0].height()
        self.x = 0
        self.y = 0
        self.current_image = 0
        self.current_image_add = 1
        self.last_time = time.time()
        self.coordinates = Coords()
        self.on_ground = False
        self.won = False
        self.facing = 'left'
        self.win_letters = []
        game.tk.bind_all('<KeyPress-Left>', self.turn_left)
        game.tk.bind_all('<KeyPress-Right>', self.turn_right)
        game.tk.bind_all('<KeyRelease-Left>', self.stop_left)
        game.tk.bind_all('<KeyRelease-Right>', self.stop_right)
        game.tk.bind_all('<space>', self.jump)

    def turn_left(self, evt):
        """
        Обрабатывает нажатие стрелки влево: устанавливает движение влево.
        Параметры: evt - событие клавиши.
        """
        self.x = -5
        self.facing = 'left'

    def turn_right(self, evt):
        """
        Обрабатывает нажатие стрелки вправо: устанавливает движение вправо.
        Параметры: evt - событие клавиши.
        """
        self.x = 5
        self.facing = 'right'

    def stop_left(self, evt):
        """
        Обрабатывает отпускание стрелки влево: останавливает движение влево.
        Параметры: evt - событие клавиши.
        """
        if self.x < 0:
            self.x = 0

    def stop_right(self, evt):
        """
        Обрабатывает отпускание стрелки вправо: останавливает движение вправо.
        Параметры: evt - событие клавиши.
        """
        if self.x > 0:
            self.x = 0

    def jump(self, evt):
        """
        Обрабатывает нажатие пробела: выполняет прыжок, если на земле.
        Параметры: evt - событие клавиши.
        """
        if self.on_ground:
            self.y = -7

    def animate_win(self):
        """
        Анимирует фонтан букв при победе с гравитацией и отскоками от платформ.
        Параметры: нет.
        """
        gravity = 0.125
        bounce = 0.8
        for letter in self.win_letters:
            letter['x'] += letter['vx']
            letter['vy'] += gravity
            letter['y'] += letter['vy']
            # Проверка столкновений с платформами
            for sprite in self.game.sprites:
                if hasattr(sprite, 'coordinates') and not sprite.endgame:
                    if letter['x'] >= sprite.coordinates.x1 and letter['x'] <= sprite.coordinates.x2 and \
                       letter['y'] >= sprite.coordinates.y1 - 20 and letter['y'] <= sprite.coordinates.y1 and letter['vy'] > 0:
                        letter['y'] = sprite.coordinates.y1 - 20
                        letter['vy'] = -letter['vy'] * bounce
            # Проверка границ земли
            if letter['y'] >= self.game.canvas_height - 20:
                letter['y'] = self.game.canvas_height - 20
                letter['vy'] = -letter['vy'] * bounce
            self.game.canvas.coords(letter['id'], letter['x'], letter['y'])
        if self.win_letters and self.win_letters[0]['y'] < self.game.canvas_height + 50:
            self.game.tk.after(50, self.animate_win)

    def animate(self):
        """
        Анимирует спрайт: меняет изображения в зависимости от направления движения.
        Параметры: нет.
        """
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
        elif self.x == 0 and self.y == 0:
            if self.facing == 'left':
                self.game.canvas.itemconfig(self.image, image=self.images_left[0])
            else:
                self.game.canvas.itemconfig(self.image, image=self.images_right[0])

    def coords(self):
        """
        Обновляет и возвращает текущие координаты спрайта на основе позиции изображения.
        Параметры: нет.
        Возвращает: объект Coords.
        """
        xy = self.game.canvas.coords(self.image)
        if self.coordinates is None:
            self.coordinates = Coords()
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + self.width
        self.coordinates.y2 = xy[1] + self.height
        return self.coordinates

    def move(self):
        """
        Обрабатывает движение спрайта: анимацию, столкновения, гравитацию и границы.
        Параметры: нет.
        """
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
            if bottom and self.y > 0 and Coords.collided_bottom(co, sprite_co):
                self.y = 0
                bottom = False
                top = False
                self.on_ground = True
            if bottom and falling and self.y == 0 and co.y2 < self.game.canvas_height and Coords.collided_bottom(co, sprite_co):
                falling = False
                self.on_ground = True
            if left and self.x < 0 and Coords.collided_left(co, sprite_co) and sprite.endgame:
                self.x = 0
                left = False
                if not self.won:
                    sprite.game.canvas.itemconfig(sprite.image, image=sprite.photo_image2)
                    self.game.canvas.itemconfig(self.image, state='hidden')
                    letters = ["П", "О", "Б", "Е", "Д", "А"]
                    for i, letter in enumerate(letters):
                        x = 200 + i * 40
                        y = 300
                        text_id = self.game.canvas.create_text(x, y, text=letter, font=("Arial", 30), fill="red")
                        self.win_letters.append({'id': text_id, 'x': x, 'y': y, 'vx': 0.125 + i * 0.025, 'vy': -3 - i * 0.2})
                    self.animate_win()
                    self.won = True
            if right and self.x > 0 and Coords.collided_right(co, sprite_co) and sprite.endgame:
                self.x = 0
                right = False
                if not self.won:
                    sprite.game.canvas.itemconfig(sprite.image, image=sprite.photo_image2)
                    self.game.canvas.itemconfig(self.image, state='hidden')
                    letters = ["П", "О", "Б", "Е", "Д", "А"]
                    for i, letter in enumerate(letters):
                        x = 200 + i * 40
                        y = 300
                        text_id = self.game.canvas.create_text(x, y, text=letter, font=("Arial", 30), fill="red")
                        self.win_letters.append({'id': text_id, 'x': x, 'y': y, 'vx': 0.125 + i * 0.025, 'vy': -3 - i * 0.2})
                    self.animate_win()
                    self.won = True
            if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
                self.y = 4
        self.game.canvas.move(self.image, self.x, self.y)
        # Гравитация
        self.y += 0.08
        xy = self.game.canvas.coords(self.image)
        if xy[1] >= self.game.canvas_height - self.height:
            self.y = 0
            self.on_ground = True
        # Ограничение границ
        if xy[0] < 0:
            self.game.canvas.coords(self.image, 0, xy[1])
            self.x = 0
        elif xy[0] > self.game.canvas_width - self.width:
            self.game.canvas.coords(self.image, self.game.canvas_width - self.width, xy[1])
            self.x = 0
        if xy[1] < 0:
            self.game.canvas.coords(self.image, xy[0], 0)
            self.y = 0
        elif xy[1] > self.game.canvas_height - self.height:
            self.game.canvas.coords(self.image, xy[0], self.game.canvas_height - self.height)
            self.y = 0
            self.on_ground = True


class DoorSprite(Sprite):
    def __init__(self, game, photo_image, x, y):
        """
        Инициализирует спрайт двери: создает изображение 1:1 и координаты на основе реальных размеров, помечает как конечный объект.
        Параметры: game - объект Game; photo_image - PhotoImage; x, y - позиция.
        """
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.photo_image2 = PhotoImage(file="./data/stickman/door2.gif")
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.width = self.photo_image.width()
        self.height = self.photo_image.height()
        self.coordinates = Coords(x, y, x + self.width, y + self.height)
        self.endgame = True


g = Game()
platform1 = PlatformSprite(g, PhotoImage(file="./data/stickman/platform1.gif"), 0, 300)
platform2 = PlatformSprite(g, PhotoImage(file="./data/stickman/platform1.gif"), 250, 580)
platform3 = PlatformSprite(g, PhotoImage(file="./data/stickman/platform1.gif"), 750, 800)
g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
door = DoorSprite(g, PhotoImage(file="./data/stickman/door1.gif"), 45, 85)
g.sprites.append(door)
player = StickFigureSprite(g)
g.sprites.append(player)
g.mainloop()
