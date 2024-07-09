# there was an error in the while loop when you calculate the xValues, yValues and the zValues
# you updated the xValue midway through the code, and then used it to calculate the other
# values. then you also updated the yValue midway through the loop and used it to calculate zValue.
# instead you should have used the values from the respective arrays so you don't make a hodgepodge.
# the changes mentioned are done and the code has been corrected.

import math
from matplotlib import pyplot as plt
# from matplotlib import numpy as np
# fx = dx/dt; fy = dy/dt; fz = dz/dt
a = 10
b = 25
c = 8/3
def fx(x,y):
    return a*(y-x)
def fy(x,y,z):
    return x*(b-z)-y
def fz(x,y,z):
    return x*y-c*z

#input step size and intial conditions and till what value to compute solution
h = 0.001 #step size of time
(xInitial, yInitial, zInitial, tInitial) = (1, 0, 0, 0) #initial condition
tFinal = 30 # time to which we want to compute the solution

itr = int((tFinal - tInitial)/h) #basically number of steps to get the final value

tValue = tInitial
xValue = xInitial
yValue = yInitial
zValue = zInitial

#arrays for the computed solution by RK4 method
tArray = [tInitial]
xArray = [xInitial]
yArray = [yInitial]
zArray = [zInitial]

count = 0
while count < itr:
    k1 = h*fx(xArray[count], yArray[count])
    k2 = h*fx(xArray[count] + 0.5*k1, yArray[count])
    k3 = h*fx(xArray[count] + 0.5*k2, yArray[count])
    k4 = h*fx(xArray[count] + k3, yArray[count])

    xValue += (k1 + 2*k2 + 2*k3 + k4)/6

    l1 = h*fy(xArray[count], yArray[count], zArray[count])
    l2 = h*fy(xArray[count], yArray[count] + 0.5+l1, zArray[count])
    l3 = h*fy(xArray[count], yArray[count] + 0.5+l2, zArray[count])
    l4 = h*fy(xArray[count], yArray[count] + l3, zArray[count])

    yValue += (l1 + 2*l2 + 2*l3 + l4)/6

    m1 = h*fz(xArray[count], yArray[count], zArray[count])
    m2 = h*fz(xArray[count], yArray[count], zArray[count] + 0.5+m1)
    m3 = h*fz(xArray[count], yArray[count], zArray[count] + 0.5+m2)
    m4 = h*fz(xArray[count], yArray[count], zArray[count] + m3)

    zValue += (m1 + 2*m2 + 2*m3 + m4)/6

    tValue += h
    xArray.append(round(xValue, 10))
    yArray.append(round(yValue, 10))
    tArray.append(round(tValue, 10))
    zArray.append(round(zValue, 10))
    count += 1

xFinal = round(xValue, 10)
yFinal = round(yValue, 10)
zFinal = round(zValue, 10)


# table of values of the computed approximate solution
# for i in range(0,len(xArray)):
#     print(xArray[i], '  ', yArray[i], '  ', zArray[i])

print('[h = ', h, '; Initial(x,y,z) = (', xInitial, ',', yInitial, ',', zInitial, ') ; Steps(itr) = ', itr , '] ', 'Final(x,y,z) = (', xFinal, ',', yFinal, ',', zFinal, ')\n')

plt.subplot(131)
plt.plot(xArray,zArray)
plt.xlabel('x')
plt.ylabel('z')
plt.grid()

plt.subplot(132)
plt.plot(yArray,zArray)
plt.xlabel('y')
plt.ylabel('z')
plt.grid()

plt.subplot(133)
plt.plot(yArray,xArray)
plt.xlabel('y')
plt.ylabel('x')
plt.grid()

plt.show()