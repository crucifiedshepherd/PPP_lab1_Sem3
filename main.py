import math
import tkinter as tk


WINDOW_SIZE = 600
CENTER = WINDOW_SIZE // 2

RADIUS = 15
DISTANCE_STEP = 3
ANGLE_STEP = math.pi * (3 - math.sqrt(5))

CIRCLE_COUNT = 100
ANIMATION_DELAY = 30


root = tk.Tk()
root.title("Простая анимация — Спираль")

canvas = tk.Canvas(
    root,
    width=WINDOW_SIZE,
    height=WINDOW_SIZE,
    bg="white"
)
canvas.pack()


def draw_circle(number):
    """Рисует один круг на заданной позиции спирали."""
    distance = number * DISTANCE_STEP
    angle = number * ANGLE_STEP

    x = CENTER + distance * math.cos(angle)
    y = CENTER + distance * math.sin(angle)

    canvas.create_oval(
        x - RADIUS,
        y - RADIUS,
        x + RADIUS,
        y + RADIUS,
        fill="red"
    )

    if number < CIRCLE_COUNT:
        root.after(
            ANIMATION_DELAY,
            draw_circle,
            number + 1
        )


draw_circle(0)

root.mainloop()
