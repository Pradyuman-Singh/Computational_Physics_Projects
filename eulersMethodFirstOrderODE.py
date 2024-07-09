import math
from matplotlib import pyplot as plt
from matplotlib import numpy as np
# input dy/dx = F(x,y);
def F(x,y):
    return 1/(1+x*y)
#input step size and intial conditions and till what value to compute solution
h = 0.2
(xInitial, yInitial) = (0,0) #initial condition
xFinal = 1

itr = int((xFinal - xInitial)/h) #basically number of steps to get the final value
xValue = xInitial
yValue = yInitial
#arrays for the computed solution by euler's method
xArray = [xInitial]
yArray = [yInitial]

count = 0
while count < itr:
    yValue += h*F(xValue, yValue)
    xValue += h
    yArray.append(round(yValue, 10))
    xArray.append(round(xValue, 10))
    count += 1
yFinal = round(yValue, 10)

#arrays for the real analytical solution
# yRealSolArray = []
# xRealSolArray = []

#inserted these two loops tompare the computed solution with the real analytical solution
# num = 1000
# for i in range(0,num+1):
#     xRealSolArray.append(xInitial + i*(xFinal - xInitial)/num)

# for x in xRealSolArray:
#     yRealSolArray.append(math.sin(x))

# table of values of the computed solution
# for i in range(0,len(xArray)):
#     print(xArray[i], '  ', yArray[i])

print(xArray)
print(yArray)
# print('[h = ', h, '; Initial = (', xInitial, ',', yInitial,') ; Steps(itr) = ', itr , '] ', 'y(',xFinal, ') = ', yFinal)
# plt.plot(xArray,yArray)
# # plt.plot(xRealSolArray,yRealSolArray)
# plt.grid()
# plt.show()