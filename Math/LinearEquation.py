import math as m
import matplotlib.pyplot as plt
print(m.floor(10.4))
x=[1,2,3,4,5]
y=[]

for i in x:
    y.append(i*2+5)

plt.plot(x,y)

# plt.scatter(x,y)
plt.xlabel('x axis')
plt.ylabel('y axix')
plt.title("linear eq")
plt.show()

