
class AmazingDog():
    __is_alive = True

    def __init__(self, animal_kind):
        self.animal_kind = animal_kind

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


class Car():
    def __init__(self, name, max_speed):
        self._name = name
        self._max_speed = max_speed
        self._speed = 0
        self._direction = 'forwards'

    def get_car_stats(self):
        return (self._name, self._max_speed)

    def get_speed_stats(self):
        return (self._speed, self._direction)

    def accelerate(self):
        #caps forwards speed at max_speed
        if self._direction == 'forwards' and self._speed >= self._max_speed:
            self._speed = self._max_speed
        #caps reverse speed at 30
        elif self._direction == 'reverse' and self._speed >= 30:
            self._speed = 30
        else:
            self._speed = self._speed + 1

    def decelerate(self):
        if self._speed > 0:
            self._speed = self._speed - 1

    def change_gear(self):
        #only changes direction if the car is stationary
        if self._speed == 0:
            if self._direction == 'forwards':
                self._direction = 'reverse'
            else:
                self._direction = 'forwards'

def test_car_class():
    mustang = Car("Mustang", 60)
    print("name:",mustang.get_car_stats()[0], " max_speed:",mustang.get_car_stats()[1])
    [mustang.accelerate() for i in range(1,100)]
    print(mustang.get_speed_stats())

    [mustang.decelerate() for i in range(1,100)]
    print(mustang.get_speed_stats())

    mustang.change_gear()
    [mustang.accelerate() for i in range(1,100)]
    print(mustang.get_speed_stats())

    [mustang.decelerate() for i in range(1,100)]
    print(mustang.get_speed_stats())

test_car_class()