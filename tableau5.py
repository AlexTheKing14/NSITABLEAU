import math

def distance(pointA, pointB):
    xA, yA = pointA
    xB, yB = pointB
    AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)
    return AB

pointA = (1, 1)
pointB = (2,2)
print(distance(pointA, pointB))