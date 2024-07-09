import math
from matplotlib import pyplot as plt
from matplotlib import numpy as np
# input y'' = d2y/dx2 = F(x,y,y') = F(x,y,p) = acclrn; y' = p = dy/dx; (t(time),x(disp),v(vel)) = (x,y,p)
# q = 0.01 #damping factor
# F_d = 1.5 #the force in forced oscillations
# w_d = 0.6 #frequency of forced oscillations
def F(x,y,p):
    return -y
#input step size and intial conditions and till what value to compute solution
h = 0.1
(xInitial, yInitial, pInitial) = (0,0,1) #initial condition
xFinal = 10

itr = int((xFinal - xInitial)/h) #basically number of steps to get the final value
# itr = whatever value you want when you dont wanna specify the final time i.e. xFinal 
# h = (xFinal - xInitial)/itr # don't forget to 'comment' the 'h' above

xValue = xInitial
yValue = yInitial
pValue = pInitial
#arrays for the computed solution by RK4 method
xArray = [xInitial]
yArray = [yInitial]
pArray = [pInitial]

count = 0
while count < itr:
    j1 = h*F(xValue, yValue, pValue)
    k1 = h*pValue
    j2 = h*F(xValue + 0.5*h, yValue + 0.5*k1, pValue + 0.5*j1)
    k2 = h*(pValue + 0.5*j1)
    

    yValue += k2
    pValue += j2
    xValue += h
    yArray.append(round(yValue, 10))
    xArray.append(round(xValue, 10))
    pArray.append(round(pValue, 10))
    count += 1
yFinal = round(yValue, 10)
pFinal = round(pValue, 10)

#arrays for the real analytical solution
# yRealSolArray = []
# xRealSolArray = []
# pRealSolArray = []

#inserted these two loops tompare the computed solution with the real analytical solution
# num = 1000
# for i in range(0,num+1):
#     xRealSolArray.append(xInitial + i*(xFinal - xInitial)/num)

# for x in xRealSolArray:
#     yRealSolArray.append(2.9*math.exp(-2*x) + 0.1*math.cos(4*x) + 0.2*math.sin(4*x))

# table of values of the computed approximate solution
# for i in range(0,len(xArray)):
#     print(xArray[i], '  ', yArray[i], '  ', pArray[i])

# print(xArray)
# print(yArray)
# print(pArray)
print('[h = ', h, '; Initial = (', xInitial, ',', yInitial, ',', pInitial, ') ; Steps(itr) = ', itr , '] ', 'y(',xFinal, ') = ', yFinal)

plt.subplot(131)
plt.plot(xArray,yArray) #plot of x vs y
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

plt.subplot(132)
plt.plot(xArray,pArray) #plot of x vs y'
plt.xlabel('x')
plt.ylabel("y'")
plt.grid()

plt.subplot(133)
plt.plot(yArray,pArray) #plot of y vs y'
plt.xlabel('y')
plt.ylabel("y'")
plt.grid()

#plt.plot(xRealSolArray,yRealSolArray)

plt.show()