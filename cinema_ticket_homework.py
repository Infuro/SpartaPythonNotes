filmDict = {"lion king": 12,
            "john whick": 18,
            "bridget jones": 0,
            "terminator": 18,
            "the prestige": 12,
            "tomas the tank engine": 0}

def films_can_watch(name, age):
    watchableFilms = []
    print(f"hello {name}, here is a list of a films you are old enough to watch:")
    [print(k) for k,v in filmDict.items() if age > v]

def error(input):
    if input == 'name':
        print('please type in a valid name')
    if input == 'age':
        print('please type in a valid age')

wrongInput = True
name = 'Null'
age = 'Null'

print("Welcome to Odeon")
while wrongInput:
    if name == 'Null':
        inputName = input("input Name: ")
        if False == inputName.isalpha() or len(inputName) > 30:
            error('name')
            pass
        name = inputName
    else:
        pass

    if age == 'Null':
        inputAge = input("input age:")
        if inputAge.isdigit() == False or len(str(inputAge)) > 3:
            error('age')
            pass
        age = int(inputAge)

    filmsCanWatch(name, int(age))
    wrongInput = False
