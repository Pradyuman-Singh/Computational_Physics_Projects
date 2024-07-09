import math
from matplotlib import pyplot as plt
# enter the function you need to find the root of
def f(x):
    return x*x - 1

xi = 2 # initial guess of the root
h = .01
print("itr", " ", "x-value", " ", "difference")
print(0, "  ", xi)
itr = 10
steps = 0 #counts the number of steps taken in the algorithm
# making a list of the x values and the steps it took to get those x values
xList = [xi]
stepsList = [steps]
xTemp = xi # stores the previous values of root to test convergence
for i in range(1, itr+1):
    xi =round( xi - 2*h*f(xi)/(f(xi+h)-f(xi-h)), 10) # using the discrete approximation for the calculation of the differentiation
    steps += 1
    xList.append(xi)
    stepsList.append(steps)
    print(i, "  ", xi, "  ", round(abs(xi - xTemp),10)) # prints the successive approximations of the root of the given functions with the iteration counter
    xTemp = round(xi, 10)

plt.plot(stepsList,xList)
plt.xlabel('Steps')
plt.ylabel('x Values[Root approximations]')
plt.grid()
plt.show()

# print(xList)
# print(stepsList)