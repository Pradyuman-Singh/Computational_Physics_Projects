import math
(a, b, n) = (0, 1, 100) # limits and steps

def f(x):
    return math.sin(x)

def sInt(a,b,n):
    h = (b-a)/n
    psum = f(a) + f(b) # initialising sum (psum = proto sum)
    for i in range(1,n):
        if i%2 == 0:
            psum += 2*f(a+i*h)
        else:
            psum += 4*f(a+i*h)
    return h*psum/3
print('Integral = ', sInt(a,b,n))