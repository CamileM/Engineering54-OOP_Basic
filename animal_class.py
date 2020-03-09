

                                    # ===== IN PSEUDO CODE =====

# 1. Define our Animal Class
class Animal():


    # 2. The CHARACTERISTICS  of every animal will include the following:
    # name, age, colour, hear, brain

    def __init__(self, name, age, colour, blood, scales):
        self.name = name
        self.age = age
        self.colour = colour
        self.heart = True
        self.brain = True

    # 3. The METHODS of every animal will include the following:
    # eat, sleep, reproduce, potty, make_sound

    def eat(self):
        return('Nom. Nom Nom')


    def sleep(self):
        return('Zzz Zzz Zzz')


    def reproduce(self):
        return('I am going to need to some privary')


    def potty(self):
        return('0_0 HMMM, o_0 AAHH! SPLOSH!! o_o')


    def make_sound(self):
        return('Woof')

# To call methods we need an object of this class

#  Creating an instance of class animal

ringo = Animal('Ringo', 200 ,'Blueish', 'BloodType', 'Snake Skin') # This creates instanes of class animal and assigns variable to ringo
# Checking and printing the instance
print(ringo)
print(type(ringo))

print('')

print(ringo.eat())
print(ringo.sleep())
print(ringo.reproduce())
print(ringo.potty())
print(ringo.make_sound())

print('')
# Check the attribute of an instance
print(ringo.name)
print(ringo.age)
print(ringo.colour)
print(ringo.brain)
print(ringo.heart)

print('')

# second animal
mini = Animal('Stacey', 25, 'Golden', 'BloodType', 'Snake Skin')
print(mini.name)
print(mini.age)
print(mini.colour)
print(mini.blood_temp)
print(mini.scales)
