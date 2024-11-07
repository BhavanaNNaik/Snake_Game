import random
from turtle import Turtle, Screen

is_race = False
screen = Screen()
screen.title('My Drawing')

screen = Screen()
screen.title('Race')
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Race", prompt="Which color will win the race")
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for i in range(0, 6):
    new_tim = Turtle(shape="turtle")
    new_tim.color(colors[i])
    new_tim.penup()
    new_tim.goto(x=-230, y=y_position[i])
    all_turtle.append(new_tim)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won, The winning color is {winning_color}")
            else:
                print(f"You lost, the winning color is {winning_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
