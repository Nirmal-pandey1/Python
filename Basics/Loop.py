for i in range(0,10):
    print(i)


list=[1,2,3,4]

for i in list:
    if i==1:
        continue
    if i==3:
        break
    print(i)
else:
    print("no break")

i=0
while i<=10:
    print("hello")
    i=i+1