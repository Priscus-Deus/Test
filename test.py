from math import sqrt
x0, y0 = 0, 0
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())

r1 = sqrt((x1 - x0) ** 2 + (y1 -y0) ** 2)
r2 = sqrt((x2 - x0) ** 2 + (y2 -y0) ** 2)
r3 = sqrt((x3 - x0) ** 2 + (y3 -y0) ** 2)

def points(x):
    point = 0
    if x <= 0.1:
        point += 3
    elif 0.1 <= x <= 0.8:
        point += 2
    elif 0.8 <= x <= 1:
        point += 1
    else:
        point += 0
    
    return point

print(points(r1) + points(r2) + points(r3))