import random
X = 640
Y = 480

B = 150
x_min = 10
y_min = B - x_min

x_distance = random.randrange(x_min, X - x_min)
y_distance = random.randrange(y_min, Y - y_min)

x = x_distance + X/2
y = y_distance + Y/2
x %= X
y %= Y

print('x    ', x)
print('y    ', y)
input()
