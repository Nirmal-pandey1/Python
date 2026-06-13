#list is [] 
#it is ordered
#it is mutable
#hetrogeneous
#it has dublicates

list=[1,2,3,4,4,5]
print(list[0])
print(list[-1])
print(list[0:4])  #sublist

list[0]=0 #mutable
print(list)

list.append("user")
print(list)

print(len(list))

# print(list.clear())
print(list.count(4))
print(list.index(4))
print(list.pop())
print(list)
list.insert(0,10)
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
list2=list.copy()

list.remove(5)
print(list2)