# Code for Object-Oriented Programming with Python - Lesson 1
# SBC - 01/12/12

###
# Slide 9 - Bear: Our first Python class
class Bear:
    print "The bear class is now defined"

a = Bear
a
# Equates a to the class Bear.  Not very useful
a = Bear()
# Creates a new *instance* of the class Bear

###
# Slide 10 - Attributes: Access, Creation, Deletion
a.name
# name attributed has not been defined yet
a.name = "Oski"
a.color = "Brown"
# new attributes are accessed with the "." operator
del(a.name)
# attributes can be deleted as well
a.name
# Throws AttributeError Exception

###
# Slide 11 - Methods: Access, Creation, and (not) Deletion
class Bear:
    print "The bear class is now defined."
    def say_hello(self):
        print "Hello, world!  I am a bear."

a = Bear()
# create a new instance of the bear class
a.say_hello
# This provides access to the method itself
a.say_hello()
# This actually executes the method

###
# Slide 12 - The __init__ method
class Bear:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print "Hello, world!  I am a bear."
        print "My name is %s." % self.name

a = Bear()
# Now you need to specify one argument to create the Bear class
a = Bear("Yogi")
a.name
a.say_hello()
# Prints desired text

###
# Slide 13 - Scope: self and "class" variables
class Bear:
    population = 0
    def __init__(self, name):
        self.name = name
        Bear.population += 1
    def say_hello(self):
        print "Hello, world!  I am a bear."
        print "My name is %s." % self.name
        print "I am number %i." % Bear.population

a = Bear("Yogi")
# Create a new instance of the Bear class.  Needs 1 argument
a.say_hello()
# Prints name and 1st bear
b = Bear("Winnie")
b.say_hello()
# Prints name and 2nd bear
c = Bear("Fozzie")
Bear.say_hello(c)
# Need "self" argument when calling directly from class

###
# Slide 15 - A Zookeeper's Travails I
class Bear:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

a = Bear("Yogi", 80)
b = Bear("Winnie", 100)
c = Bear("Fozzie", 115)
# Create three new Bear instances
my_bears = [a, b, c]
# Combine them into a list
total_weight = 0
for z in my_bears:
    total_weight += z.weight

# Loop over the list and add to the total weight
total_weight < 300
# The zookeeper only needs to make one trip.

###
# Slide 17 - A Zookeeper's Travails II
class Bear:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def eat(self, amount):
        self.weight += amount
    def hibernate(self):
        self.weight /= 1.20

a = Bear("Yogi", 80)
b = Bear("Winnie", 100)
c = Bear("Fozzie", 115)
my_bears=[a, b, c]
a.weight
a.eat(20)
a.weight
# After eating, Yogi gains 20 kg
b.eat(10)
# Winnie eats
c.hibernate()
# Fozzie hibernates`
total_weight = 0
for z in my_bears:
    total_weight += z.weight

total_weight < 300
# Now the keeper needs two trips.

###
# Slide 19 - A Zookeeper's Travails III
class Bear:
    def __init__(self, name, fav_food, friends=[]):
        self.name = name
        self.fav_food = fav_food
        self.friends = friends
    def same_food(self):
        for friend in self.friends:
            if (friend.fav_food == self.fav_food):
                print "%s and %s both like %s" % \
                 (self.name, friend.name, self.fav_food)

a = Bear("Yogi", "Picnic baskets")
b = Bear("Winnie", "Honey")
c = Bear("Fozzie", "Frog legs")

###
# Slide 20 - A Zookeeper's Travails III
c.friends	# empty list
c.fav_food	# 'Frog legs'
c.same_food()	# Returns None since no friends
c.friends = [a, b]	# Now Fozzie has two friends
c.same_food()	# But still no overlap in food tastes
c.fav_food = "Honey"	# Fozzie now likes honey
c.same_food()	# And shares same food with Winnie




