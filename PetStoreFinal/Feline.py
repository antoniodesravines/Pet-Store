#Antonio DesRavines
#Comp163-004
#03-21-2024
#This program introduces the feline class

#Imports classes needed for inheritance
from Mammal import Mammal

class Feline(Mammal):

    # Defines attributes for class
    def __init__(self, size='', weight=0.00, color=''):
        Mammal.__init__(self)
        self.size = size
        self.weight = weight
        self.color = color

    #Getters and setters
    def purr(self, purrAmount):
        print('purr' * purrAmount)

    def getSize(self):
        return self.size

    def setSize(self, sizeValue):
        self.size = sizeValue

    def getWeight(self):
        return self.weight

    def setWeight(self, weightValue):
        self.weight = weightValue

    def getColor(self):
        return self.color

    def setColor(self, colorValue):
        self.color = colorValue