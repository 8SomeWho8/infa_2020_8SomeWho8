from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class target():
    def __init__(self):
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.r = 0
        self.color = '#ccff00'
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)

    def new_target(self, x_min=600, x_max=800, y_min=300, y_max=550):
        """ Инициализация новой цели. """
        self.r = rnd(5, 50)
        self.x = rnd(x_min + self.r, x_max - self.r)
        self.y = rnd(y_min + self.r, y_max - self.r)
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)

    def move(self):
        if self.x + self.vx > 800 - self.r:
            self.x = 2 * (800 - self.r) - self.x - self.vx
            self.vx *= -1
        elif self.x + self.vx < 0 + self.r:
            self.x = 2 * self.r - self.x - self.vx
            self.vx *= -1
        else:
            self.x += self.vx
        if self.y + self.vy > 600 - self.r:
            self.y = 2 * (600 - self.r) - self.y - self.vy
            self.vy *= -1
        elif self.y + self.vy < 0 + self.r:
            self.y = 2 * self.r - self.y - self.vy
            self.vy *= -1
        else:
            self.y += self.vy
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def hit(self):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 1
        self.color = choice(['red', '#ff7f50', 'blue', 'green', '#b666d2', 'yellow', 'cyan', '#ffbf00', '#711919'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if abs(self.vx) > 1e-1:
            self.vx += self.ax
            if self.x + self.vx > 800 - self.r:
                self.x = 2 * (800 - self.r) - self.x - self.vx
                self.vy *= 0.7
                self.vx *= -0.7
            else:
                self.x += self.vx
        if abs(self.vx) > 1e-1 or self.y - self.r >= 600:
            self.vy += self.ay
            if self.y + self.vy > 600 - self.r:
                self.y = 2 * (600 - self.r) - self.y - self.vy
                self.vy *= -0.5
                self.vx *= 0.5
            else:
                self.y += self.vy
        else:
            self.y = 600 - self.r - 3
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def hittest(self, obj: target):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5 <= self.r + obj.r:
            return True
        else:
            return False


class gun():

    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
points = 0
id_points = canv.create_text(30, 30, text=points, font='28')
canv.itemconfig(id_points, text=points)
balls = []


def new_game(event=''):
    global g1, t1, screen1, balls, bullet, points
    t1.new_target()
    t2.new_target()
    while ((t1.x - t2.x)**2 + (t1.y - t2.y)**2)**0.5 <= t1.r + t2.r:
        t2.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    z = 0.01
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or balls:
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                points += 1
                canv.itemconfig(id_points, text=points)
                t1.hit()
            if b.hittest(t2) and t2.live:
                t2.live = 0
                points += 1
                canv.itemconfig(id_points, text=points)
                t2.hit()
            if not t1.live and not t2.live:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
            if b.y == 600 - b.r - 3:
                b.live -= 1
            if b.live == 0:
                canv.delete(b.id)
                balls.remove(b)
        if t1.live:
            t1.move()
        if t2.live:
            t2.move()
        canv.update()
        time.sleep(z)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(g1)
    root.after(20, new_game())


new_game()

root.mainloop()
