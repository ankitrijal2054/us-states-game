from turtle import Turtle

#FONT = ("Courier", 24, "normal")


class WriteState(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def display_state(self, state, x, y):
        self.goto(int(x), int(y))
        self.write(f"{state}")
