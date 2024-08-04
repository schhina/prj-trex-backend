from random import random
import math

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def generateRandomStar(cls):
        return Star(random()*100, random()*100)
    
    def __repr__(self):
        return f"({self.x},{self.y})"

class ShootingStar(Star):
    maxVel = 50
    def __init__(self, x, y, v_x, v_y):
        self.v_x = v_x
        self.v_y = v_y
        super().__init__(x, y)
    
    @classmethod
    def generateRandomSStar(cls):
        if (random() > 0.5):
            x = round(random())*100
            y = random()*100
        else:
            y = round(random())*100
            x = random()*100
        v_x = (random() - 0.5)*cls.maxVel*2
        v_y = math.sqrt(cls.maxVel**2 - v_x**2) * (-1 if random() > 0.5 else 1)
        return ShootingStar(x, y, v_x, v_y)

    def __repr__(self):
        return f"{self.x},{self.y},{self.v_x},{self.v_y}"
