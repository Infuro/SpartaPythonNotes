from animal import Animal

class Reptile(Animal):
    def __init__(self):
        super().__init__()
        self.cold_blooded = True

    def __repr__(self):
        return f'this is a reptile'
    #returns a representation of the object

    def __str__(self):
        return f'string version of a reptile'
    #changes the output for when the object is printed

    def use_venom(self):
        print("use venom because im a reptile")

    def move(self):
        print("move as a snake")

print("im a snake")
snake = Reptile()
snake.use_venom()
snake.move()


