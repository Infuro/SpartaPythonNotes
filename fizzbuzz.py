def fizzbuzz(number: int):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        pass
#[(print(i), fizzbuzz(i)) for i in range(1,100)]

def division(int1:int = 4, int2:int = 2) -> float:
    return int1/ int2
#specifies returning a float with  -> float
#int1:int = 4

