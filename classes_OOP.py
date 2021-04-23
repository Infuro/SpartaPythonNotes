class AmazingDog():
    __is_alive = True

    def __init__(self, animal_kind):
        self.animal_kind = animal_kind
        self.bark()

    def set_is_alive(self, alive_status):
        self.__is_alive = alive_status

    def get_is_alive(self):
        return self.__is_alive

    def bark(self):
        print("woof!")

jason = AmazingDog("canine")
sue = AmazingDog("dolphin")

#an underscore in front of a variable tells others not to use it directly
#print(sue.__is_alive)
#^doesnt work
#if you know its there you can access it in python

#instead we use getters and setters
sue.set_is_alive(True)
print(sue.get_is_alive())





#create a ccar class
#max speed
#current speed
#minus speed?
#reverse numbers?
