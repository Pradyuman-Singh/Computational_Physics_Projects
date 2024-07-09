import math
from matplotlib import pyplot as plt
from matplotlib import numpy as np
# input y'' = d2x/dt2 = F(t,x,dx/dt) = F(t,x,v) = acclrn; x' = v = dx/dt; (t(time),x(disp),v(vel)) = (x,y,p)
# q = 0.5   #first  order damping factor
# F_d = 1.5 #the force in forced oscillations
# w_d = 0.6 #frequency of forced oscillations
def F(t,x,v):
    return -x
#input step size and intial conditions and till what value to compute solution
h = 0.00001 #step size in time
(tInitial, xInitial, vInitial) = (0,1,0) #initial condition
tFinal = 10

itr = round(((tFinal - tInitial)/h)) #basically number of steps to get the final value
# itr = whatever value you want when you dont wanna specify the final time i.e. xFinal 
# h = (xFinal - xInitial)/itr # don't forget to 'comment' the 'h' above

tValue = tInitial
xValue = xInitial
vValue = vInitial
#arrays for the computed solution by RK4 method
tArray = [tInitial]
xArray = [xInitial]
vArray = [vInitial]

count = 0
while count < itr:
    j1 = h*F(tValue, xValue, vValue)
    k1 = h*vValue
   
    xValue += k1
    vValue += j1
    tValue += h
    xArray.append(round(xValue, 10))
    tArray.append(round(tValue, 10))
    vArray.append(round(vValue, 10))
    count += 1
xFinal = round(xValue, 10)
vFinal = round(vValue, 10)

#arrays for the real analytical solution
# tRealSolArray = []
# xRealSolArray = []
# vRealSolArray = []

#inserted these two loops tompare the computed solution with the real analytical solution
# num = 1000
# for i in range(0,num+1):
#     tRealSolArray.append(tInitial + i*(tFinal - tInitial)/num)

# for x in tRealSolArray:
#     xRealSolArray.append(some function)

# table of values of the computed approximate solution
# for i in range(0,len(tArray)):
#     print(tArray[i], '  ', xArray[i], '  ', vArray[i])

# print(tArray)
# print(xArray)
# print(vArray)
print('[h = ', h, '; Initial = (', tInitial, ',', xInitial, ',', vInitial, ') ; Steps(itr) = ', itr , ']\n', 'x(',tFinal, ') =', xFinal, ';  v(',tFinal, ') =', vFinal)

plt.subplot(131)
plt.plot(tArray,xArray) #plot of time vs disp
plt.xlabel('Time')
plt.ylabel('Disp')
plt.grid()

plt.subplot(132)
plt.plot(tArray,vArray) #plot of time vs velocity
plt.xlabel('Time')
plt.ylabel('Vel')
plt.grid()

plt.subplot(133)
plt.plot(xArray,vArray) #plot of time vs velocity
plt.xlabel('Disp')
plt.ylabel('Vel')
plt.grid()

#plt.plot(tRealSolArray,xRealSolArray)

plt.show()