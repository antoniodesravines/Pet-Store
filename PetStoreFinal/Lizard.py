#Antonio DesRavines
#Comp163-004
#03-21-2024
#This program introduces the lizard class

#Imports classes needed for inheritance
from Reptile import Reptile

class Lizard(Reptile):

    # Defines attributes for class
    def __init__(self, size='', weight=0.00, color='', habitat='', frill=True, spikes=True):
        Reptile.__init__(self)
        self.size = size
        self.weight = weight
        self.color = color
        self.habitat = habitat
        self.frill = frill
        self.spikes = spikes

    # Getters and setters
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

    def getHabitat(self):
        return self.habitat

    def setHabitat(self, newHabitat):
        self.habitat = newHabitat

    def hasFrill(self):
        return self.frill

    def setFrill(self, newFrill):
        self.frill = newFrill

    def hasSpikes(self):
        return self.spikes

    def setSpikes(self, newSpikes):
        self.spikes = newSpikes