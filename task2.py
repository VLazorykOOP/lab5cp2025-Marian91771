import turtle

def koch(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch(t, length, depth - 1)
        t.left(60)
        koch(t, length, depth - 1)
        t.right(120)
        koch(t, length, depth - 1)
        t.left(60)
        koch(t, length, depth - 1)

def draw_koch_square(length, depth):
    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(-200, 200)
    t.pendown()

    for _ in range(4):
        koch(t, length, depth)
        t.right(90)

    turtle.done()

draw_koch_square(300, 3)
