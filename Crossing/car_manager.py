from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random

class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.speed=STARTING_MOVE_DISTANCE
        self.chance=6

    def create_car(self):
        random_x=random.randint(1,self.chance)
        if random_x ==1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.setheading(180)
            random_y=random.randint(-250,250)
            car.goto(300,random_y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT




