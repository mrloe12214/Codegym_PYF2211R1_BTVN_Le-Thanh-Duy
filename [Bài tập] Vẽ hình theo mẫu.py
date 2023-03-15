import turtle

r = int(input("nhập r = "))
t = turtle.Turtle()
t.speed(0)
colors = ["red", "green", "blue", "purple", "orange", "yellow"]
color_index = 0
angle = 0
while angle <= 360:

    t.pencolor(colors[color_index])
    color_index += 1
    if color_index == len(colors):
        color_index = 0

    for i in range(2):
        t.circle(r,90)
        t.circle(r//2,90)

    t.goto(0, 0)
    t.pendown()

    angle += 10
    t.right(10)

turtle.done()
