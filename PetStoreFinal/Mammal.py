#Antonio DesRavines
#Comp163-004
#03-21-2024
#This program introduces the mammal class

#Imports classes needed for inheritance
from Animal import Animal

class Mammal(Animal):

    # Defines attributes for class
    def __init__(self):
        Animal.__init__(self)
        self.warmBlooded = True
        self.fur = True

    # Getters and setters
    def isWarmBlooded(self):
        return self.warmBlooded

    def setWarmBlooded(self, isWarmBlooded):
        self.warmBlooded = isWarmBlooded

    def hasFur(self):
        return self.fur

    def setFur(self, isFur):
        self.fur = isFur

