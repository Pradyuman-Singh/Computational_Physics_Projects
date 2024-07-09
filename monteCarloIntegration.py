import math
import random

def f(x,y,z):
    return 8*x*y*z

count = 0
num = 3000000
sum = 0

(xi, xf) = (2, 3)
(yi, yf) = (1, 2)
(zi, zf) = (0, 1)

dx = xf - xi
dy = yf - yi
dz = zf - zi

for i in range(num):
    # x = random.randrange(xi*num,xf*num,1)/num
    # y = random.randrange(yi*num,yf*num,1)/num
    x = random.uniform(xi, xf)
    y = random.uniform(yi, yf)
    z = random.uniform(zi, zf)
    sum += f(x,y,z)*dx*dy*dz

integral = round(sum/num, 10)
print(integral)