import turtle

# Vẽ ngôi nhà
house = turtle.Turtle()

house.penup()
house.goto(-100, 100)
house.pendown()
house.color("light yellow")
house.begin_fill()
for i in range(4):
    house.forward(200)
    house.right(90)
house.end_fill()
house.penup()
house.goto(-100, 100)
house.pendown()
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
window.penup()
window.goto(-25, -100)
window.pendown()

window.color("black")
window.begin_fill()
window.forward(50)
window.left(90)
window.forward(75)
window.left(90)
window.forward(50)
window.left(90)
window.forward(75)
window.end_fill()

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

# Vẽ cây
tree = turtle.Turtle()

tree.penup()
tree.goto(-200, -100)
tree.pendown()

tree.color("green")
tree.begin_fill()
tree.left(90)
tree.forward(150)
tree.right(90)
tree.forward(20)
tree.right(90)
tree.forward(150)
tree.end_fill()

tree.penup()
tree.goto(-265, 75)
tree.pendown()
tree.color("light green")
tree.begin_fill()
tree.circle(75)
tree.end_fill()

turtle.done()
