import turtle

# Vẽ ngôi nhà
house = turtle.Turtle()

house.penup()
house.goto(-100, 100)
house.pendown()
house.color("light yellow")
house.begin_fill()
house.forward(200)
house.right(90)
house.forward(200)
house.right(90)
house.forward(200)
house.right(90)
house.forward(200)
house.right(90)
house.end_fill()
# Vẽ ống khói
house.penup()
house.goto(85, 100)
house.pendown()

house.color("light yellow")
house.begin_fill()
house.left(90)
house.forward(50)
house.right(90)
house.forward(15)
house.right(90)
house.forward(50)
house.right(90)
house.end_fill()

#Vẽ mái
house.penup()
house.goto(-100, 100)
house.pendown()

house.right(180)
house.color("red")
house.begin_fill()
house.left(45)
house.forward(141)
house.right(90)
house.forward(141)
house.end_fill()
# Vẽ cửa sổ
window = turtle.Turtle()

window.penup()
window.goto(-75, 75)
window.pendown()
window.color("gray")
window.begin_fill()
for i in range(4):
    window.forward(50)
    window.right(90)
window.end_fill()

window.penup()
window.goto(25, 75)
window.pendown()
window.begin_fill()
for i in range(4):
    window.forward(50)
    window.right(90)
window.end_fill()

#Vẽ cửa chính
door = turtle.Turtle()

door.penup()
door.goto(-25, -100)
door.pendown()

door.color("black")
door.begin_fill()
door.forward(50)
door.left(90)
door.forward(75)
door.left(90)
door.forward(50)
door.left(90)
door.forward(75)
door.end_fill()
# Vẽ mặt trời
sun = turtle.Turtle()

sun.penup()
sun.goto(250, 250)
sun.pendown()
sun.color("yellow")
sun.begin_fill()
for i in range(12):
    sun.forward(75)
    sun.backward(75)
    sun.left(30)
sun.end_fill()

sun.penup()
sun.goto(250, 200)
sun.pendown()
sun.color("red")
sun.begin_fill()
sun.circle(50)
sun.end_fill()
# Vẽ cây 1
tree = turtle.Turtle()

tree.penup()
tree.goto(-200, -100)
tree.pendown()

tree.color("green")
tree.begin_fill()
tree.left(90)
tree.forward(120)
tree.right(90)
tree.forward(20)
tree.right(90)
tree.forward(120)
tree.end_fill()

x = -295
y = 20
a = 150
tree.left(45)
for i in range(1,4):
    tree.penup()
    tree.goto(x, y)
    tree.pendown()
    tree.left(45)
    tree.color("light green")
    tree.begin_fill()
    tree.left(45)
    tree.forward(a)
    tree.right(90)
    tree.forward(a)
    tree.end_fill()
    y+=50
    x+=10
    a-=20

# Vẽ cây 2
tree.penup()
tree.goto(300, -50)
tree.pendown()
tree.left(45)

tree.color("green")
tree.begin_fill()
tree.left(90)
tree.forward(85)
tree.right(90)
tree.forward(20)
tree.right(90)
tree.forward(85)
tree.end_fill()

x = 240
y = 30
a = 100
tree.left(45)
for i in range(1,4):
    tree.penup()
    tree.goto(x, y)
    tree.pendown()
    tree.left(45)
    tree.color("light green")
    tree.begin_fill()
    tree.left(45)
    tree.forward(a)
    tree.right(90)
    tree.forward(a)
    tree.end_fill()
    y+=35
    x+=10
    a-=20
turtle.done()
