"""
sumlist = []
for i in range(0,1000):
    if i % 3 == 0 or i % 5 == 0:
        sumlist.append(i)
print(sum(sumlist))

def fibaRecurs(first, second):
    if second > 4000000:
        return
    first + second + fibaRecurs(first, second)


def fibo(x):
    print(x, " ", end="")
    if x > 10:
        return x
    else:
        return x + fibo(x+1)

sumlist = []
def two_val_fibo(first, second):
    if first % 2 == 0:
        sumlist.append(first)
    if first > 4000000:
        return first
    else:
        return (first + second) + two_val_fibo(second, (first + second))
two_val_fibo(1, 2)
print(sum(sumlist))



list = [i for i in range(2,21)]
def even_divi():
    for i in range(1,1000000000):
        count = 0
        for j in list:
            if i % j == 0:
                count += 1
        if count == 19:
            return i
print(even_divi())



def strange():
    list1 = list(range(1,10))
    print("first:", list1)
    for i in list1:
        print(i)
        list1.pop()
    return list1
print(strange())


            if len(str(i)) == 3 and (int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])) % 3 == 0:

#abirame's method
prime=int(input('Enter a range: '))
p=[]
for j in range(2,prime):
    for i in range(2,prime):
        if j!=i:
            if j%i==0:
               # print(f'{j} not a prime number')
                break
        else:
            #print(f'{j} is a prime number')
            p.append(j)
print(sum(p))

def prime_time():
    primes = []
    primes.append(5)
    for i in range(2,2000001):
        if i % 2 != 0 and i % 5 != 0:
            for j in primes:
                if i * j
            primes.append(i)
    return primes
print(sum(prime_time()))
"""

def strange():
    list1 = ["a", "b", "c", "d", "e", "f"]
    list2 = []
    for i in list1:
        list2.append(i)
        list1.remove(i)
    return (list1, list2)
print(strange())
