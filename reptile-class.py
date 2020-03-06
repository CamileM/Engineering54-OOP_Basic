from animal_class import *


class Reptile(Animal):

    def __init__(self, name, age, colour, scales,blood_temp):
        super().__init__(name, age, colour)
        self.blood_temp = blood_temp
        self.scales = scales

    pass

    def make_sound(self):
        return('GRWWLLLL, GRWWLWLLWLL')

    def hunt(self):
        return

    def seek_sun(self):
        return

    def seek_shade(self):
        return


animal1 = Animal('Nacho', 20, 'Yellowish')
print(animal1)

print('')

# Reptile has all the attribute and method of Animal
reptile1 = Reptile('Ringo', 200, 'Blueish')
print(reptile1.name) # This is a attribute of a reptile not a method
print(reptile1.eat())
print(reptile1.potty())
print(reptile1.sleep())
print(reptile1.reproduce())
print(reptile1.make_sound())




