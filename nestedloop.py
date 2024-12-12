import turtle
turtle.shape("turtle")
turtle.speed(0)
for side_legth in range(50,1000):
    for i in range(5):
        turtle.forward(side_legth)
        turtle.left(45)

    turtle.exitonclick