from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
color = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

user_choise = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-125 + turtle_index * 50)
    turtles.append(new_turtle)

is_race_on = False

if user_choise:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choise:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()