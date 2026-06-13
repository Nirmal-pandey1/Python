# function is a block of code  that can be executed by calling function name
def sum(a,b):
    return a+b

print(sum(10,20))
# parameter which is mention in function defination
#argument which is passed during function call

# argument are 3 types
#positional agrument as we seen above 10 will assigned to a and 20 to b
#default argument
def greet(name="admin"):
    print(f"wellcome {name}")

greet()
greet("nirmal")

# keyword argument
def show(a,b):
    print(f"a={a},b={b}")

show(b=19,a=10)