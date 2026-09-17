import math
import tkinter as tk


WINDOW_SIZE = 600
CENTER = WINDOW_SIZE // 2

MIN_RADIUS = 6
MAX_RADIUS = 15
DISTANCE_STEP = 3
# ANGLE_STEP = math.radians(20)
ANGLE_STEP = math.pi * (3 - math.sqrt(5))

CIRCLE_COUNT = 100
STEM_COUNT = 7

ANIMATION_DELAY = 30
GROW_STEPS = 5
GROW_DELAY = 20


root = tk.Tk()
root.title("Простая анимация — Спираль")

canvas = tk.Canvas(
    root,
    width=WINDOW_SIZE,
    height=WINDOW_SIZE,
    bg="white"
)
canvas.pack()


def get_circle_color(number):
    """Определяет цвет точки в зависимости от этапа роста."""
    if number < STEM_COUNT:
        return "green"

    if number < 40:
        return "yellow"

    if number < 70:
        return "pink"

    return "red"


def get_circle_radius(number):
    """Определяет конечный размер точки."""
    radius = MIN_RADIUS + number * 0.1
    return min(radius, MAX_RADIUS)


def grow_circle(number, step, item_id, target_radius):
    """Постепенно увеличивает размер одной точки."""
    radius = target_radius * step / GROW_STEPS

    distance = number * DISTANCE_STEP
    angle = number * ANGLE_STEP

    x = CENTER + distance * math.cos(angle)
    y = CENTER + distance * math.sin(angle)

    canvas.coords(
        item_id,
        x - radius,
        y - radius,
        x + radius,
        y + radius
    )

    if step < GROW_STEPS:
        root.after(
            GROW_DELAY,
            grow_circle,
            number,
            step + 1,
            item_id,
            target_radius
        )
    elif number < CIRCLE_COUNT:
        root.after(
            ANIMATION_DELAY,
            draw_circle,
            number + 1
        )


def draw_circle(number):
    """Создаёт новую точку и запускает её рост."""
    distance = number * DISTANCE_STEP
    angle = number * ANGLE_STEP

    x = CENTER + distance * math.cos(angle)
    y = CENTER + distance * math.sin(angle)

    color = get_circle_color(number)
    target_radius = get_circle_radius(number)

    item_id = canvas.create_oval(
        x,
        y,
        x,
        y,
        fill=color,
        outline=""
    )

    grow_circle(
        number,
        1,
        item_id,
        target_radius
    )


draw_circle(0)

root.mainloop()