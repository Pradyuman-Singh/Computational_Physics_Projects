import math
from matplotlib import pyplot as plt
from matplotlib import numpy as np
# input y'' = d2y/dx2 = F(x,y,y') = F(x,y,p) = acclrn; y' = p = dy/dx; (t(time),x(disp),v(vel)) = (x,y,p)
# q = 0.01 #damping factor
# F_d = 1.5 #the force in forced oscillations
# w_d = 0.6 #frequency of forced oscillations
I = 800
E = 3 * 10**4
P = 1
L = 10
def F(x,y,p):
    return -P*(L-x)/(E*I)
#input step size and intial conditions and till what value to compute solution
h = 0.1
(xInitial, yInitial, pInitial) = (0,0,0) #initial conditions;
xFinal = 50

itr = int((xFinal - xInitial)/h) #basically number of steps to get the final value
# itr = whatever value you want when you dont wanna specify the final time i.e. xFinal 
# h = (xFinal - xInitial)/itr # don't forget to 'comment' the 'h' above

xValue = xInitial
yValue = yInitial
pValue = pInitial
#creating and initialising the arrays for the computed solution by RK4 method
xArray = [xInitial]
yArray = [yInitial]
pArray = [pInitial]

# print('\nTable(RK-4 SOLUTION): \nSteps = ', 0, '; ', 'Output: y(', xValue, ')   = ', yValue )

count = 0
while count < itr:
    j1 = h*F(xValue, yValue, pValue)
    k1 = h*pValue
    j2 = h*F(xValue + 0.5*h, yValue + 0.5*k1, pValue + 0.5*j1)
    k2 = h*(pValue + 0.5*j1)
    j3 = h*F(xValue + 0.5*h, yValue + 0.5*k2, pValue + 0.5*j2)
    k3 = h*(pValue + 0.5*j2)
    j4 = h*F(xValue + h, yValue + k3, pValue + j3)
    k4 = h*(pValue + j3)

    yValue += (k1 + 2*k2 + 2*k3 + k4)/6
    pValue += (j1 + 2*j2 + 2*j3 + j4)/6
    xValue += h
    yArray.append(round(yValue, 10))
    xArray.append(round(xValue, 10))
    pArray.append(round(pValue, 10))
    count += 1
    # print('Steps = ', count, '; ', 'Output :y(', round(xValue,10), ') = ', round(yValue, 10)) # prints the table for computed solution
yFinal = round(yValue, 10)
pFinal = round(pValue, 10)

# arrays for the real analytical solution
# yRealSolArray = []
# xRealSolArray = []
# pRealSolArray = []

# inserted these two loops to compare the computed solution with the real analytical solution
# num = 1000
# for i in range(0,num+1):
#     xRealSolArray.append(xInitial + i*(xFinal - xInitial)/num) # DO NOT CHANGE THIS LOOP

# for x in xRealSolArray:
#     yRealSolArray.append(-P*L*x*x/(2*E*I) + P*x*x*x/(6*E*I)) # Enter the function you want to plot in terms of 'x' in the append bracket

# table of values of the computed approximate solution
# for i in range(0,len(xArray)):
#     print(xArray[i], '  ', yArray[i], '  ', pArray[i]) # If you want to print the table of values of the analytical(real) solution

# print(xArray)
# print(yArray)
# print(pArray)
print('[Step size: h = ', h, '; Initial(x, y, y\') = (', xInitial, ',', yInitial, ',', pInitial, ') ; Steps(itr) = ', itr , '] ', ' Output : y(',xFinal, ') = ', yFinal)


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

# plt.subplot(122)
# plt.plot(xRealSolArray,yRealSolArray) #plot of x vs y
# plt.xlabel('x')
# plt.ylabel("y")
# plt.grid()
# plt.title('Elastic curve for a Cantilever - Analytical solution')

plt.show()