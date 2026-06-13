#mutable
#not ordered
#duplicates contain --no
#hetrogeneous


s={1,2,3,4,4,5}
print(s)
s.add(10)
# s.clear()
# s.remove
s2={9,11,12}
print(s.difference(s2))
print(s2.difference(s))
print(s.union(s2))
print(s.intersection(s2))
print(s.isdisjoint(s2))
s.discard(49) #no error if element is not present


print(s|s2) # | union & intersection - difference ^ symmetric_diffrence
# s.remove(30)  error



