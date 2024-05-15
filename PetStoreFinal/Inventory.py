#Antonio DesRavines
#Comp163-004
#03-21-2024
#This program introduces the inventory class

class Inventory:

    #Defines attributes for class
    def __init__(self, location='N/A', quantity=0, price=0.0):
        self.location = location
        self.quantity = quantity
        self.price = price

    #Getters and setters
    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price

    def getLocation(self):
        return self.location

    def setQuantity(self, newQuantity):
        self.quantity = newQuantity

    def setPrice(self, newPrice):
        self.price = newPrice

    def setLocation(self, newLocation):
        self.location = newLocation