def fizzbuzz(number: int):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz", end=", ")
    elif number % 5 == 0:
        print("buzz", end=", ")
    elif number % 3 == 0:
        print("fizz", end=", ")
    else:
        print(number, end=", ")
#[(print(i), fizzbuzz(i)) for i in range(1,100)]

def division(int1:int = 4, int2:int = 2) -> float:
    return int1/ int2
#specifies returning a float with  -> float
#int1:int = 4

