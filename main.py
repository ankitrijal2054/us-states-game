import turtle
import pandas
from write_state import WriteState

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

display = WriteState()

data = pandas.read_csv("50_states.csv")
list_of_state = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer == "Exit":
        break

    if answer in list_of_state:
        guessed_states.append(answer)
        state_info = data[data.state == answer]
        state_name = state_info.state
        x_value = state_info.x
        y_value = state_info.y
        display.display_state(answer, x_value, y_value)

missed_state = []
for state in list_of_state:
    if state in guessed_states:
        continue
    else:
        missed_state.append(state)

sv = pandas.DataFrame(missed_state)
sv.to_csv("state_to_learn.csv")
