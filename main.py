from tkinter import *
from ball import Ball
from platform import Platform
from enemy_platform import Enemy_platform
import time

window = Tk()

window.title("ping-pong")
window.geometry("500x400")
window.resizable(False, False)
window.wm_attributes("-topmost", 1)

canvas = Canvas(window, width=500, height=400)
canvas.pack()

platform = Platform(canvas, "purple")
ball = Ball(canvas, platform, "red")
enemy_platform = Enemy_platform(canvas, "black", ball)
ball.enemy_platform = enemy_platform

while True:
    if ball.touched == False:
        platform.draw()
        ball.draw()
        enemy_platform.draw()
    else:
        break

    time.sleep(0.01)
    window.update()
