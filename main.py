import math
import tkinter as tk


WINDOW_SIZE = 600
CENTER = WINDOW_SIZE // 2
RADIUS = 20

DISTANCE = 100
ANGLE = math.radians(45)


def draw_circle():
    """Рисует один круг на заданном расстоянии и под заданным углом."""
    x = CENTER + DISTANCE * math.cos(ANGLE)
    y = CENTER + DISTANCE * math.sin(ANGLE)

    canvas.create_oval(
        x - RADIUS,
        y - RADIUS,
        x + RADIUS,
        y + RADIUS,
        fill="red"
    )


root = tk.Tk()
root.title("Простая анимация — Спираль")

canvas = tk.Canvas(
    root,
    width=WINDOW_SIZE,
    height=WINDOW_SIZE,
    bg="white"
)
canvas.pack()

draw_circle()

root.mainloop()