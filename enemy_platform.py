class Enemy_platform:
    def __init__(self, canvas, color, ball):
        self.canvas = canvas
        self.color = color
        self.rect = canvas.create_rectangle(230, 50, 330, 60, fill=color)
        self.x = 0
        self.ball = ball

    def draw(self):
        ball_coord = self.canvas.coords(self.ball.oval)
        self.canvas.move(self.rect, self.x, 0)
        pos = self.canvas.coords(self.rect)

        # x0 - левая точка
        if pos[0] <= 0:
            self.x = 0
        # x1 - правая точка
        if pos[2] >= 500:
            self.x = 0

        # x0 - левая точка
        if ball_coord[0] <= pos[0]:
            self.x = -3

        # x1 - правая точка
        if ball_coord[2] >= pos[2]:
            self.x = 3