class Platform:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.x = 0

        # привязываю кнопки
        self.canvas.bind_all("<KeyPress-Left>", self.left)
        self.canvas.bind_all("<KeyPress-Right>", self.right)
        self.canvas.bind_all("<KeyRelease>", self.stop)

    def stop(self, event):

        self.x = 0  # скорость

    def left(self, event):

        self.x = -2  # скорость

    def right(self, event):

        self.x = 2  # скорость

    def draw(self):
        self.canvas.move(self.rect, self.x, 0)  # двигаю платформу по x
        pos = self.canvas.coords(self.rect)  # узнаю координаты платформы
        # x0 - левая точка
        if pos[0] <= 0:
            self.x = 0
        # x1 - правая точка
        if pos[2] >= 500:
            self.x = 0

