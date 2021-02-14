from turtle import Turtle, Screen

franklin = Turtle()
screen = Screen()


def move_forward():
    franklin.forward(10)


def move_backward():
    franklin.backward(10)


def turn_clockwise():
    franklin.right(10)


def turn_not_clockwise():
    franklin.left(10)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_not_clockwise)
screen.onkey(key="c", fun=screen.reset)


screen.exitonclick()
