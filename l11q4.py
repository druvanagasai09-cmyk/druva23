square = lambda x: x* x
cube = lambda x: x* x
maximum = lambda a, b: a if a > b else b

number = float(input("enter a number :"))

print("square =",  square(number))
print("cube=", cube(number))

a = float (input("enter first number :"))
b = float (input("enter second number :"))

print("maximum =", maximum(a , b))