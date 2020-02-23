# libraries
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import numpy as np
import math

# Data
'data x is dx, etc'
dx = [3,6,7,78,92]
dy = [0.75,0.70,0.80,1.28,1.60]
colors = (0, 0, 0)
area = 2*np.pi*3

fun_str = input("Enter function of x: ")
x_min = min(dx) #int(input("Enter minimum: "))
x_max = max(dx) #int(input("Enter maximum: "))
ns = x_max

# Parameters
sum_x = sum(dx)
sum_ysqr = sum(dy)
print("sum y^2: ", sum_ysqr)



xs = range(1,100) #np.linspace(x_min, x_max, ns)
print(sum(xs))
ys = []

for x in xs:
    y = eval(fun_str)
    ys.append(y)

ye = []
yss = []

print(ys)
print(dy)
for i in range(len(dx)):
    print("i and x", i, dx[i])
    print("prediction: x and y", dx[i],ys[dx[i]] )
    yss.append(ys[dx[i]])
    ye.append(dy[i]-yss[i])

print(yss)
print(ye)

# Plot
plt.style.use('seaborn-whitegrid')
plt.scatter(yss, ye, s=area, color='black', alpha=0.5)
plt.xlabel('Predicted')
plt.ylabel('Residual')
plt.show()

# Plot
plt2.style.use('seaborn-whitegrid')
plt2.plot(xs, ys, c='red', linestyle='dashed', alpha=0.7)
plt2.scatter(dx, dy, s=area, color='black', alpha=0.5)
plt2.xlabel('Days')
plt2.ylabel('Elapsed Time')
plt2.title('Linear Regression')
plt2.show()