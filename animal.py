class Animal:
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("breathes")

    def move(self):
        print("moves all directions")

    def eat(self):
        print("eats")

#this only runs if this file is run directly, if imported it doesnt run
print(__name__)
if __name__ == '__main__':
    print("im a cat")
    cat = Animal()
    cat.move()