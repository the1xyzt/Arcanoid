import random
class Ball:
    #
    def __init__(self, canvas, platform, color):
        self.canvas = canvas
        self.platform = platform
        self.enemy_platform = None
        self.color = color
        self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.dir = [-3, -2, -1, 0, 1, 2, 3]
        self.x = random.choice(self.dir)
        self.y = -1
        self.touched = False

    def touch_platform(self, ball_pos):
        platform_coord = self.canvas.coords(self.platform.rect)
        enemy_platform_coord = self.canvas.coords(self.enemy_platform.rect)
        if ball_pos[0] <= platform_coord[2] and ball_pos[2] >= platform_coord[0]:
            if ball_pos[3] >= platform_coord[1] and ball_pos[3] <= platform_coord[3]:
                return 1

        if ball_pos[0] <= enemy_platform_coord[2] and ball_pos[2] >= enemy_platform_coord[0]:
            if ball_pos[1] >= enemy_platform_coord[1] and ball_pos[1] <= enemy_platform_coord[3]:
                return 2
        return False

    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)  # двигаю платформу по x
        pos = self.canvas.coords(self.oval)  # узнаю координаты платформы

        # y0 - верхняя точка
        if pos[1] <= 0:
            self.y = 3
        # y1 - нижняя точка
        if pos[3] >= 400:
            self.touched = True  # проиграл
        # x0 - левая точка
        if pos[0] <= 0:
            self.x = 3

        # x1 - правая точка
        if pos[2] >= 500:
            self.x = -3
        # если коснулся платформы моей
        if self.touch_platform(pos) == 1:
            self.y = -3

        # если коснулся платформы врага
        if self.touch_platform(pos) == 2:
            self.y = 3
