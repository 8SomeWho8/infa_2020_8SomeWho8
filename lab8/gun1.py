from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
canv.focus_set()


class target():
    def __init__(self):
        """
        Конструктор класса Target
        """
        self.live = 1  # Переменная, отвечающая за существование цели.
        # Равна 1, если цель не поражена, равна 0, если она не поражена.
        self.id = canv.create_oval(0, 0, 0, 0)  # Объект овала в tkinter, соответсвующий рисованию цели
        # Начальные координаты и скорости цели по осям
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        # Радиус цели
        self.r = 0
        # Цвет цели
        self.color = '#ccff00'
        # Задание характеристик овала с заданными координатами
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)

    def new_target(self, x_min=0, x_max=800, y_min=0, y_max=600):
        """ Инициализация новой цели с новыми случайными координатами, скоростями и радиусом. """
        self.r = rnd(5, 50)
        self.x = rnd(x_min + self.r, x_max - self.r)
        self.y = rnd(y_min + self.r, y_max - self.r)
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)

    def move(self):
        """
        Передвижение цели с постоянной скоростью, а также отражение её от стен
        """
        if self.x + self.vx > 800 - self.r:  # Условие отражения от правой стены
            self.x = 2 * (800 - self.r) - self.x - self.vx
            self.vx *= -1
        elif self.x + self.vx < 0 + self.r:  # Условие отражения от левой стены
            self.x = 2 * self.r - self.x - self.vx
            self.vx *= -1
        else:
            self.x += self.vx
        if self.y + self.vy > 600 - self.r:  # Условие отражения от пола
            self.y = 2 * (600 - self.r) - self.y - self.vy
            self.vy *= -1
        elif self.y + self.vy < 0 + self.r:  # Условие отражения от потолка
            self.y = 2 * self.r - self.y - self.vy
            self.vy *= -1
        else:
            self.y += self.vy
        # Обновление координат объекта tkinter
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def hit(self):
        """Попадание шарика в цель. Она перемещается в невидимую часть экрана"""
        canv.coords(self.id, -10, -10, -10, -10)


class ball():
    def __init__(self, x=-40, y=0):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        # Начальные координаты, скорости и ускорения шарика по осям
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 1
        # Фиксированнный радиус шарика
        self.r = 10
        # Случайный цвет шарика
        self.color = choice(['red', '#ff7f50', 'blue', 'green', '#b666d2', 'yellow', 'cyan', '#ffbf00', '#711919'])
        # Создание объекта tkinter
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        # Переменная жизни шарика, при её обнулении экзмепляр удаляется
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы ускорений self.ax, self.ay,
        и стен (от которых мяч отражается) по краям окна (размер окна 800х600).
        """
        if abs(self.vx) > 1e-1:  # условие остановки по оси х
            self.vx += self.ax
            if self.x + self.vx > 800 - self.r:  # условие отражения от правой стены
                self.x = 2 * (800 - self.r) - self.x - self.vx
                # потеря энергии от сооударений с правой стеной
                self.vy *= 0.7
                self.vx *= -0.7
            else:
                self.x += self.vx
        if abs(self.vx) > 1e-1 or self.y + self.r < 597:  # условие остановки по оси у
            self.vy += self.ay
            if self.y + self.vy > 600 - self.r:  # условие отражения от "пола"
                self.y = 2 * (600 - self.r) - self.y - self.vy
                # потеря энергии от сооударений с "полом"
                self.vy *= -0.5
                self.vx *= 0.5
            else:
                self.y += self.vy
        else:
            self.y = 600 - self.r - 3  # остановка по оси у, т. е. сохранение вертикальной координаты на уровне "пола"
        # Обновление координат объекта из tkinter
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
            obj: Обьект, с которым проверяется столкновение. В нашем случае с шариком.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5 <= self.r + obj.r:  # Условие сближения центров
            # шарика и цели на расстояние, меньшее суммы их радиусов
            return True
        else:
            return False


class gun():
    def __init__(self):
        """
        Инициализация класса gun
        """
        # Коэффициент, отвечающий за модуль начальной скорости вылетающего шарика,
        # а также за удлинение пушки перед выстрелом
        self.f2_power = 10
        # Переменная, показывающая, начата ли подготовка перед выстрелом или нет
        self.f2_on = 0
        # Координаты пушки в начале игры
        self.x = 50
        self.y = 570
        # Переменная скорости горизонтального движения пушки
        self.v = 5
        # Переменная угла наклона пушки к горизонтали(со знаком)
        self.an = 1
        # Объект "линии" из tkinter
        self.body_length = 40
        self.body_height = 15
        self.right_wheel_rad = 6
        self.right_wheel_colour = choice(['red', '#ff7f50', 'blue', 'green', '#b666d2',
                                          'yellow', 'cyan', '#ffbf00', '#711919'])
        self.left_wheel_rad = 6
        self.left_wheel_colour = choice(['red', '#ff7f50', 'blue', 'green', '#b666d2',
                                         'yellow', 'cyan', '#ffbf00', '#711919'])
        self.barrel = canv.create_line(self.x, self.y,
                                       self.x + 25 * math.cos(math.pi / 4), self.y + 25 * math.sin(math.pi / 4),
                                       width=7)
        self.body_colour = choice(['red', '#ff7f50', 'blue', 'green', '#b666d2',
                                   'yellow', 'cyan', '#ffbf00', '#711919'])
        self.body = canv.create_rectangle(self.x - self.body_length / 2, self.y - 2,
                                          self.x + self.body_length / 2, self.y + self.body_height,
                                          fill=self.body_colour)
        self.left_wheel = canv.create_oval(self.x - self.body_length / 4 - self.right_wheel_rad,
                                           self.y + self.body_height,
                                           self.x - self.body_length / 4 + self.right_wheel_rad,
                                           self.y + self.body_height + 2 * self.right_wheel_rad,
                                           fill=self.right_wheel_colour)
        self.right_wheel = canv.create_oval(self.x + self.body_length / 4 - self.left_wheel_rad,
                                            self.y + self.body_height,
                                            self.x + self.body_length / 4 + self.left_wheel_rad,
                                            self.y + self.body_height + 2 * self.left_wheel_rad,
                                            fill=self.left_wheel_colour)

    def fire2_start(self, event=''):  # Начало подготовки к выстрелу, в течении которой f2_power растёт
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1  # Количество потраченных шариков
        new_ball = ball()  # Будущий снаряд
        new_ball.r += 5
        # Задание начальных координат нового снаряда как координат пушки в момент выстрела
        new_ball.x = self.x
        new_ball.y = self.y
        # Вычисление угла наклона пушки, зависит от положения мыши
        if (event.x - self.x) > 0 and (event.y - self.y < -0.3 * (event.x - self.x)):
            self.an = math.atan((event.y - self.y) / (event.x - self.x))
        elif (event.x - self.x) > 0 and (event.y - self.y >= -0.3 * (event.x - self.x)):
            self.an = math.atan(-0.3)
        elif (event.x - self.x) < 0 and (event.y - self.y < 0.3 * (event.x - self.x)):
            self.an = math.pi + math.atan((event.y - self.y) / (event.x - self.x))
        elif (event.x - self.x) < 0 and (event.y - self.y >= 0.3 * (event.x - self.x)):
            self.an = math.pi + math.atan(0.3)
        elif (event.x == self.x) and self.y >= event.y:
            self.an = -math.pi / 2
        # Задание начальных скоростей снаряда по осям, пропорционально силе f2_power
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]  # Добавление снаряда в общий массив "живых" снарядов
        self.f2_on = 0  # Окончание подготовки к выстрелу
        self.f2_power = 10  # Восстановление начальной силы выстрела

    def targetting(self, mouse_x, mouse_y):
        """Прицеливание. Зависит от положения мыши."""
        # Вычисление угла наклона пушки к вертикали
        if (mouse_x - self.x) > 0 and (mouse_y - self.y < -0.3 * (mouse_x - self.x)):
            self.an = math.atan((mouse_y - self.y) / (mouse_x - self.x))
        elif (mouse_x - self.x) > 0 and (mouse_y - self.y >= -0.3 * (mouse_x - self.x)):
            self.an = math.atan(-0.3)
        elif (mouse_x - self.x) < 0 and (mouse_y - self.y < 0.3 * (mouse_x - self.x)):
            self.an = math.pi + math.atan((mouse_y - self.y) / (mouse_x - self.x))
        elif (mouse_x - self.x) < 0 and (mouse_y - self.y >= 0.3 * (mouse_x - self.x)):
            self.an = math.pi + math.atan(0.3)
        elif (mouse_x == self.x) and self.y >= mouse_y:
            self.an = -math.pi / 2
        if self.f2_on:  # Рисование оранжевой пушки, если идёт подготовка к выстрелу
            canv.itemconfig(self.barrel, fill='orange')
        else:  # Рисование чёрной пушки в обратном случае
            canv.itemconfig(self.barrel, fill='black')
        # Обновление координат объекта пушки из tkinter, длина пушки зависит от f2_power
        canv.coords(self.barrel, self.x, self.y,
                    self.x + max(self.f2_power * 5 / 18 + 200 / 9, 25) * math.cos(self.an),
                    self.y + max(self.f2_power * 5 / 18 + 200 / 9, 25) * math.sin(self.an)
                    )

    def power_up(self):
        """
        Увеличение f2_power по мере подготовки к выстрелу, с ограничением сверху в 100 условных пунктов
        """
        # Смена цвета пушки в случае, если она готовится к выстрелу
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.barrel, fill='orange')
        else:
            canv.itemconfig(self.barrel, fill='black')

    def move_right(self, event=''):
        """
        Передвижение пушки вправо по горизонтали
        """
        if self.x < 780:
            self.x += self.v
        canv.coords(
            self.barrel,
            self.x,
            self.y,
            self.x + max(self.f2_power * 5 / 18 + 200 / 9, 25) * math.cos(self.an),
            self.y + max(self.f2_power * 5 / 18 + 200 / 9, 25) * math.sin(self.an)
        )
        canv.coords(
            self.body,
            self.x - self.body_length / 2,
            self.y - 2,
            self.x + self.body_length / 2,
            self.y + self.body_height,
        )
        canv.coords(
            self.left_wheel,
            self.x - self.body_length / 4 - self.right_wheel_rad,
            self.y + self.body_height,
            self.x - self.body_length / 4 + self.right_wheel_rad,
            self.y + self.body_height + 2 * self.right_wheel_rad,
        )
        canv.coords(
            self.right_wheel,
            self.x + self.body_length / 4 - self.left_wheel_rad,
            self.y + self.body_height,
            self.x + self.body_length / 4 + self.left_wheel_rad,
            self.y + self.body_height + 2 * self.left_wheel_rad,
        )

    def move_left(self, event=''):
        """
        Передвижение пушки влево по горизонтали
        """
        if self.x > 20:
            self.x -= self.v
        canv.coords(
            self.barrel,
            self.x,
            self.y,
            self.x + max(self.f2_power * 5 / 18 + 200 / 9, 25) * math.cos(self.an),
            self.y + max(self.f2_power * 5 / 18 + 200 / 9, 25) * math.sin(self.an)
        )
        canv.coords(
            self.body,
            self.x - self.body_length / 2,
            self.y - 2,
            self.x + self.body_length / 2,
            self.y + self.body_height,
        )
        canv.coords(
            self.left_wheel,
            self.x - self.body_length / 4 - self.right_wheel_rad,
            self.y + self.body_height,
            self.x - self.body_length / 4 + self.right_wheel_rad,
            self.y + self.body_height + 2 * self.right_wheel_rad,
        )
        canv.coords(
            self.right_wheel,
            self.x + self.body_length / 4 - self.left_wheel_rad,
            self.y + self.body_height,
            self.x + self.body_length / 4 + self.left_wheel_rad,
            self.y + self.body_height + 2 * self.left_wheel_rad,
        )


class mouse_cords():
    def __init__(self):
        self.x = 0
        self.y = 0

    def new_cords(self, event):
        self.x = event.x
        self.y = event.y


# Создание двух экземпляров класса target
t1 = target()
t2 = target()
# Создание объекта из tkinter, отвечающего за вывод текста после уничтожения всех мишеней
screen1 = canv.create_text(400, 300, text='', font='28')
# Создание экземпляра класса gun
g1 = gun()
# Создание глобальных переменных, отвечающих за количество потраченных шариков и количество полученных очков
bullet = 0
points = 0
# Создание объекта из tkinter, отвечающего за вывод количества очков
id_points = canv.create_text(30, 30, text=points, font='28')
canv.itemconfig(id_points, text=points)
# Создание глобального массива с "живыми" шариками
balls = []

mc = mouse_cords()

def new_game():
    global g1, t1, screen1, balls, bullet, points, mc
    # Задание мишеням случайных координат
    t1.new_target()
    t2.new_target()
    # Поиск координат для второй мишени, чтобы та не пересекалась с первой
    while ((t1.x - t2.x) ** 2 + (t1.y - t2.y) ** 2) ** 0.5 <= t1.r + t2.r:
        t2.new_target()
    # Обнуление глобальной переменной, отвечающей за количество потраченных шариков
    bullet = 0
    # "Опустошение" глобального массива с "живыми" шариками
    balls = []
    # Связь зажатия левой кнопки мыши с функцией начала подготовки к выстрелу
    canv.bind('<Button-1>', g1.fire2_start)
    # Связь отпускания левой кнопки мыши с функцией выстрела
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    # Связь движения мыши с функцией прицеливания
    canv.bind('<Motion>', mc.new_cords)
    # Связь нажатия стрелок на клавиатуре с движением пушки по горизонтали
    canv.bind('<d>', g1.move_right)
    canv.bind('<a>', g1.move_left)
    # Задание переменной, отвечающей за время ожидания между отрисовками последовательных кадров
    z = 1 / 144
    # Восстановление переменных жизни целей
    t1.live = 1
    t2.live = 1
    # Основной цикл игры, условие прекращения которого - отсутствующие на поле шарики и все поражённые мишени
    while t1.live or t2.live or balls:
        for b in balls:  # Действия для всех шариков из массива со всеми "живыми" шариками
            b.move()  # Передвижение шарика за одну единицу времени
            # Проверка столкновения шариков с целями, добавление очков за поражение целей,
            # обновление переменной жизни целей, а также удаление поражённых целей
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
            # Условие "прекращения огня" для вывода результатов уничтожения мишеней
            if not t1.live and not t2.live:
                # Привязывание кликов мыши к пустым событиям для отсутствия шариков между играми
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
            if b.y == 600 - b.r - 3:  # Проверка условия остановки шарика
                b.live -= 1  # Уменьшение срока жизни шарика для последующего его удаления после остановки
            if b.live == 0:  # Удаление "мёртвых" шариков с полотна и из массива "живых" шариков
                canv.delete(b.id)
                balls.remove(b)

        # Проверка условия жизни мишени и перемещение живых мишеней
        if t1.live:
            t1.move()
        if t2.live:
            t2.move()
        canv.update()
        # Задержка между кадрами
        time.sleep(z)
        g1.targetting(mc.x, mc.y)
        g1.power_up()
    # Стирание текста о количестве потраченных шариков перед новой игрой
    canv.itemconfig(screen1, text='')
    canv.delete(g1)
    root.after(20, new_game())  # Вызов функции new_game для старта новой игры по окончании текущей


new_game()

root.mainloop()
