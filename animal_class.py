
# define our Animal Class

# Pseudo Code
    # Looks / Characteristic of every animal
    # name, age, colour, hear, brain

    # Behaviours / Methods of every animal
    # eat, sleep, reproduce, potty, make_sound

class Animal():

    # define behaviour and characteristics

    # define the characteristics of EVERY animal

    def __init__(self, name, age, colour, blood, scales):
        self.name = name
        self.age = age
        self.colour = colour
        self.heart = True
        self.brain = True


    # define behaviour and characteristics

    # Defining the method .eat(), .sleep(), .reproduce(), .potty(), .make_sound()
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

ringo = Animal('Ringo', 200 ,'Blueish') # This creates instanes of class animal and assigns variable to ringo
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
mini = Animal('Stacey', 25, 'Golden')
print(mini.name)
print(mini.age)
print(mini.colour)

