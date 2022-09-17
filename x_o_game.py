from turtle import *


p1 = Turtle()
p1.shape('triangle')
p1.color('green')
p1.penup()
p1.goto(-30, 90)


p2 = Turtle()
p2.shape('triangle')
p2.color('blue')
p2.penup()
p2.goto(-30, 0)



def squad_f(f, x, y):
    f.penup()
    f.goto(x + 30, y)
    f.pendown()
    f.goto(x + 30, y + 30)
    f.goto(x, y + 30)
    f.goto(x, y)


def game_place():
    gp = Turtle()
    gp.speed(0)
    gp.color('red')
    gp.begin_fill()
    for x in range(0, 61, 30):
        for y in range(0, 61, 30):
            squad_f(gp, x, y)
    gp.penup()
    gp.goto(0, 0)
    gp.pendown()
    gp.goto(90, 0)
    gp.hideturtle()


game_place()


# def get_area1(x, y):
    # begin_fill()
    # p1.pendown()
    # p1.goto(x, y)
    # p1.filling()
    # p2.end_fill()


p1.ondrag(goto, btn=1, add=())


# def get_area2(x, y):
    # p2.begin_fill()
    # p2.pendown()
    # p2.goto(x, y)
    # p2.filling()
    # p2.end_fill()

p2.ondrag(goto, btn=2, add=())


done()