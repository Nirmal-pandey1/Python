# ordered
# key unique value duplicate 
# mutable

dict={}
dict['name']="nirmal"
dict["age"]="30"
print(dict)
print(dict.get("name"))
for i in dict.keys():
    print(f"{i}:{dict.get(i)}")

# for key,value in dict.items:
#     print(key)
#     print(value)

print(dict.values)
dict.update({"name":"raj"})
print(dict)

# dict.pop("name")
# dict.popitem()