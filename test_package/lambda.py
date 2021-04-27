def addFun(num1, num2):
    return (num1 + num2)

print(addFun(1,2))

addLam = lambda num1, num2: num1 + num2

print(addLam(1,2))

addLam = lambda num1=1, num2=2: num1 + num2

print(addLam())

print((lambda num1, num2: num1 + num2)(1,2))

list = [i for i in range(1,15)]
squarelist = map((lambda x: x^2), list)
print(list(squarelist))