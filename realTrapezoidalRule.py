import math
(a, b, n) = (0, 1, 10000) # limits and steps

def f(x):
    return math.sin(x)

def tInt(a,b,n):
    h = (b-a)/n
    psum = 0.5*(f(a) + f(b)) # initialising sum (psum = proto sum)
    for i in range(1,n):
        psum += f(a+i*h)
    return h*psum
print('Integral = ', tInt(a,b,n))