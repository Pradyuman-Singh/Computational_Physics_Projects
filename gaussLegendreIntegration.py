import math

# sort the abcissae array in increasing order
# for five point:
# w = [0.23692689, 0.47862867, 0.56888889, 0.47862867, 0.23692689]
# x = [-0.90617985, -0.53846931, 0, 0.53846931, 0.90617985]
# for ten point:
w = [0.0666713443086881, 0.1494513491505806, 0.2190863625159820, 0.2692667193099963, 0.2955242247147529]
w += w[::-1] # reverses the order of list and appends it to itself; i.e. [1,2,3] will become [1,2,3,3,2,1]
x = [-0.9739065285171717, -0.8650633666889845, -0.6794095682990244, -0.4333953941292472, -0.1488743389816312]
temp_x = x # make a temporary copy of the abscissae list
temp_x = [-i for i in x] # reverse the signs of the temp list abscissae
x += temp_x[::-1] # add the reversed temp list to original abscissae list
temp_x.clear()
# code for ten point gauss-legendre list manipulation ends here

(a,b) = (-1, 1) # limits

p = 0.5*(b-a)
q = 0.5*(b+a)

def f(x):
    return math.atan(x)*math.log(0.5*(1+x*x))/(1+x)

def g(x):
    return f(p*x + q)

sum = 0
for i in range(len(w)):
    sum += w[i]*g(x[i])

int = p*sum
print('Integral = ', int)