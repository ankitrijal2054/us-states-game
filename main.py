import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

named_state = 0

data = pandas.read_csv("50_states.csv")
list_of_state = data["state"].to_list()
print(list_of_state)

while named_state < 50:
    answer = screen.textinput(title=f"{named_state}/50 States Correct", prompt="What's another state's name?")
    if answer.lower() in list_of_state.lower():
        state_info = data[data.state.lower() == answer.lower()]
        




screen.exitonclick()