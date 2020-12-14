from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place Your Bet", prompt="Which Turtle wil win the race?:  ")
print(user_bet)
colour_list = ["red", "yellow", "green", "purple", "blue", "hot pink"]
y_position = [-80, -40, 0, 40, 80, 120]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour_list[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You Won! the {winning_colour} turtle is the winner")
            else:
                print(f"You Lost! the {winning_colour} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
