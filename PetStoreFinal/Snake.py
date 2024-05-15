#Antonio DesRavines
#Comp163-004
#03-21-2024
#This program introduces the snake class

#Imports classes needed for inheritance
from Reptile import Reptile

class Snake(Reptile):

    # Defines attributes for class
    def __init__(self, size='', weight=0.00, color='', constrictor=True, food=''):
        Reptile.__init__(self)
        self.size = size
        self.weight = weight
        self.color = color
        self.constrictor = constrictor
        self.food = food

    #Getters and setters
    def getSize(self):
        return self.size

    def setSize(self, newSize):
        self.size = newSize

    def getWeight(self):
        return self.weight

    def setWeight(self, newWeight):
        self.weight = float(newWeight)

    def getColor(self):
        return self.color

    def setColor(self, newColor):
        self.color = newColor

    def getFood(self):
        return self.food

    def setFood(self, newFood):
        self.food = newFood

    def isConstrictor(self):
        return self.constrictor

    def setConstrictor(self, newConstrictor):
        self.constrictor = newConstrictor