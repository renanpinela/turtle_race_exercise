from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race? Enter a color: ('Red', 'Orange', 'Yellow', 'Green', 'Blue' or 'Purple'?) ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    newturtle = Turtle("turtle")
    newturtle.penup()
    newturtle.color(colors[turtle_index])
    newturtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(newturtle)

if user_bet == "red" or user_bet == "orange" or user_bet == "yellow" or user_bet == "green" or user_bet == "blue" or user_bet == "purple":
    is_race_on = True
else:
    print('You have not entered a valid color.')

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()