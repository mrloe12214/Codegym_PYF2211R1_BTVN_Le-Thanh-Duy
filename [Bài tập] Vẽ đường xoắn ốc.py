import turtle

b = int(input("nhập khoảng cách: "))
distance = 0
a = 1
turtle.speed(0) # Đặt tốc độ vẽ là tối đa
turtle.goto(0,0)

while True:
    turtle.forward(a)
    turtle.right(10)
    distance += a
    a += 0.1
    if distance > b:
        break

turtle.done()
