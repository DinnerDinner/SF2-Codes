from __future__ import annotations

import math

#Classes
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    def translate(self, dx, dy):
        self.x += dx
        self.y+=dy
    def distance(self, other_point:Point):
        a = (other_point.x - self.x) ** 2
        b = (other_point.y - self.y)**2
        return math.sqrt(a+b)
    def __repr__(self)-> str:
        return f'({self.x}, {self.y})'


p1 = Point(2,3)
print(f"(x,y) coordinates of p1: {p1.x}, {p1.y}")

p1.translate(4, 2)
print(f'(x,y) coordinates of p1: ({p1.x}, {p1.y})')
