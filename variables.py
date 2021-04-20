"""
variable_name = "hello world!"
a = 20
b = 6.7

print(variable_name)
name = input("what is your name? :")
age = input("what is ur age?? :")
height = input("how tall are you in cm?? :")
dob = input("what is your dob? :")
print(f"hello {name}, you are {age} years old and also you are {height}m tall, your dob is {dob}")

print(type(a), ' ', type(b))
print(a + b)

float = 3.2
print(int(3.2))

#slicing strings:
hi = "hello world"
print(hi[0:12:2])
print(hi[::-1])
#python slicing includes the first digit and excludes second digit.. a half closed interval

print(hi.count("l"))
print(hi.upper())

a = 40
b = input("number")
#doesnt work:
#print(a + b)

#does work:
print(str(a) + b)

"""

#BOOLEANS -----------------------------------------------------

hi = "hello world"

print(hi.isalpha())
print(hi.isnumeric())
print(hi.isdigit())
print(hi.isdecimal())
print(hi.endswith("d"))

#Truthy and falsey
#https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/
z == None))