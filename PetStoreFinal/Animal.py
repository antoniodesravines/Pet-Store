#Antonio DesRavines
#Comp163-004
#03-21-2024
#This program introduces the animal class

#Imports classes needed for inheritance
from Inventory import Inventory

class Animal:

    # Defines attributes for class
    def __init__(self, multiCellular=True, sexualReproduction=True, heteroTroph=True, fourLimbs=True, backbone=True, Type='Animal', name='', inventory=Inventory()):
        Inventory.__init__(self)
        self.multiCellular = multiCellular
        self.sexualReproduction = sexualReproduction
        self.heterotroph = heteroTroph
        self.fourLimbs = fourLimbs
        self.backbone = backbone
        self.Type = Type
        self.name = name
        self.inventory = inventory

    # Getters and setters
    def isMultiCellular(self):
        return self.multiCellular

    def hasSexualReproduction(self):
        return self.sexualReproduction

    def isHeterotroph(self):
        return self.heterotroph

    def hasFourLimbs(self):
        return self.fourLimbs

    def setFourLimbs(self, fourLimbs):
        self.fourLimbs = fourLimbs

    def hasBackbone(self):
        return self.backbone

    def getName(self):
        return self.Name

    def setName(self, Name):
        self.Name = Name

    def setInventory(self, location, quantity, price):
        self.inventory = Inventory(location, quantity, price)