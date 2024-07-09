import random
from matplotlib import pyplot as plt

l = 0.01
N = 100

N_Array = [N]
t_Array = [0]
count = 0

while N: # i.e. while number of particles are not zero
    for i in range(N):
        if random.random() < l: # selection of roughly l fraction of particles that will decay from a total of N particles
            N = N-1
    count += 1
    N_Array.append(N)
    t_Array.append(count)

# print(N_Array)
# print(t_Array)
plt.plot(t_Array, N_Array)
plt.xlabel('Time')
plt.ylabel('Num')
plt.grid()
plt.show()