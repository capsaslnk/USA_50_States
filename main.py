import turtle
import pandas

# Creating of the screen to the game
screen = turtle.Screen()
screen.title("U.S. 50 States Game")
screen.addshape("download.gif")
turtle.shape("download.gif")

from turtle import Turtle

# Creating of the turtle to printout the state names
word = Turtle()
word.hideturtle()
word.color("black")
word.penup()

# Reading of the data file
data = pandas.read_csv("50_states.csv")

# Setting up game starting data
game_is_on = True
score = 0
guessed_states = []

# Creating the logic to game
while game_is_on:
    state = screen.textinput(
        title=f"{score}/50 Guess the state name", prompt="What's a other state name"
    ).title()

    # Creating an exit for game with missing states csv as a output
    if state == "Exit":

        # Filtering of data from series
        states_to_learn = data[~data["state"].isin(guessed_states)]["state"]
        states_to_learn.to_csv("filtered_states.csv")
        break

    if state in data.state.to_list():
        guessed_state = data[data.state == state]
        guessed_states.append(state)

        # Getting the value only from the x series
        # guessed_state.x.item() == guessed_state.x.values[0]
        word.goto(guessed_state.x.values[0], guessed_state.y.values[0])
        word.write(state)
        score += 1
        if score == 50:
            game_is_on = False
