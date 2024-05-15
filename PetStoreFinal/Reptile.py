#Antonio DesRavines
#Comp163-004
#03-21-2024
#This program introduces the reptile class

#Imports classes needed for inheritance
from Animal import Animal

class Reptile(Animal):

    # Defines attributes for class
    def __init__(self):
        Animal.__init__(self)
        self.coldBlooded = True
        self.food = 'Live'
        self.attribute = 'Reptile'

    # Getters and setters
    def isColdBlooded(self):
        return self.coldBlooded

    def getFood(self):
        return self.getFood

    def setFood(self, newFood):
        self.food = newFood