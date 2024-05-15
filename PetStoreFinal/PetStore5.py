#Antonio DesRavines
#Comp163-004
#05-01-2024
#This program modifies pet store 4 project to save and load pet store data

#Imports csv file to be read into python
import csv

#Imports classes needed for inheritance
from Canine import Canine
from Feline import Feline
from Snake import Snake
from Lizard import Lizard


#Defines the pets list
pets = ['Canine', 'Feline', 'Snake', 'Lizard']

#Defines inventory dictionary
inventory = {}

#Defines bill of sale dictionary
billOfSale = {}

#Initial welcome statement
print('Welcome to the Aggie Pet Store')

#Create canine function
def createCanine(dictionary):
    numOfCanines = int(input(f'How many canines are you entering: '))
    dictionary['Canine'] = []

    for i in range(numOfCanines):
        #Asks for pet attributes
        petName = input(f'What is the type of canine: ')
        petSize = input(f'What is the size of canine: ')
        petWeight = float(input(f'What is the weight of canine: '))
        petColor = input(f'What is the color of canine: ')
        petLocation = input(f'What is the location of canine: ')
        petQuantity = input('What is the quantity of the canine you are entering: ')
        petPrice = float(input(f'What is the cost per canine: '))

        #Creates pet and stores it in dictionary
        dictionary['Canine'].append(Canine(petSize, petWeight, petColor))
        dictionary['Canine'][i].setName(petName)
        dictionary['Canine'][i].setInventory(petLocation, petQuantity, petPrice)

#Create feline function
def createFeline(dictionary):
    numOfFelines = int(input(f'How many felines are you entering: '))
    dictionary['Feline'] = []

    for i in range(numOfFelines):
        # Asks for pet attributes
        petName = input(f'What is the type of feline: ')
        petSize = input(f'What is the size of feline: ')
        petWeight = float(input(f'What is the weight of feline: '))
        petColor = input(f'What is the color of feline: ')
        petLocation = input(f'What is the location of feline: ')
        petQuantity = int(input(f'What is the quantity of the feline you are entering: '))
        petPrice = float(input(f'What is the cost per feline: '))

        # Creates pet and stores it in dictionary
        dictionary['Feline'].append(Feline(petSize, petWeight, petColor))
        dictionary['Feline'][i].setName(petName)
        dictionary['Feline'][i].setInventory(petLocation, petQuantity, petPrice)

#Create snake function
def createSnake(dictionary):
    numOfSnakes = int(input('How many snakes are you entering: '))
    dictionary['Snake'] = []
    for i in range(numOfSnakes):
        #Collects pet attributes
        petName = input(f'What is the type of snake: ')
        petSize = input(f'What is the size of snake: ')
        petWeight = float(input(f'What is the weight of snake: '))
        petColor = input(f'What is the color of snake: ')
        petConstrictor = bool(input('Is this snake a constrictor?(True/False): '))
        petFood = input('What type of food does the snake eat:')
        petLocation = input(f'What is the location of snake: ')
        petQuantity = int(input(f'What is the quantity of the snake you are entering: '))
        petPrice = float(input(f'What is the cost per snake: '))

        #Adds new pet to dictionary
        dictionary['Snake'].append(Snake(petSize, petWeight, petColor, petConstrictor, petFood))
        dictionary['Snake'][i].setName(petName)
        dictionary['Snake'][i].setInventory(petLocation, petQuantity, petPrice)

#Create lizard function
def createLizard(dictionary):
    numOfLizards = int(input('How many reptiles are you entering: '))
    dictionary['Lizard'] = []
    for i in range(numOfLizards):
        #Collects pet attributes
        petName = input(f'What is the type of lizard: ')
        petSize = input(f'What is the size of lizard: ')
        petWeight = float(input(f'What is the weight of lizard: '))
        petColor = input(f'What is the color of lizard: ')
        petHabitat = input('What is the habitat of the lizard: ')
        petFrill = bool(input('Does this lizard have frills?(True/False): '))
        petSpikes = bool(input('Does this lizard have spikes?(True/False): '))
        petLocation = input(f'What is the location of lizard: ')
        petQuantity = int(input(f'What is the quantity of the lizard you are entering: '))
        petPrice = float(input(f'What is the cost per lizard: '))

        #Stores them inside a dictionary
        dictionary['Lizard'].append(Lizard(petSize, petWeight, petColor, habitat=petHabitat, frill=petFrill, spikes=petSpikes))
        dictionary['Lizard'][i].setName(petName)
        dictionary['Lizard'][i].setInventory(petLocation, petQuantity, petPrice)

def loadPetstore(dictionary):
    with open('PetStore.csv', 'r') as csvFile:
        csvReader = csv.reader(csvFile)


        #Creates variable to check first row of the csv file
        firstRow = next(csvReader)

        #If the first cell of the file is empty, set up store
        if firstRow[0] == 'empty':
            setupStore()

        #If file is not empty, load in data from file and use this for petstore
        else:
            #Reset filereader to beginning of file (first line gets skipped over while checking if empty)
            csvFile.seek(0)

            #Set up inventory dictionary
            dictionary['Canine'] = []
            dictionary['Feline'] = []
            dictionary['Snake'] = []
            dictionary['Lizard'] = []

            #Counters to keep track of how many of each animal have been entered, helps with iteration
            canineCount = 0
            felineCount = 0
            snakeCount = 0
            lizardCount = 0

            #For loop to iterate through csv with pet store data
            for row in csvReader:
                #If-elif statements to determine what type of pet is in that row of the csv
                if row[0] == 'Canine':
                    #Creates canine object in inventory based on csv attributes
                    dictionary['Canine'].append(Canine(row[2], float(row[3]), row[4]))
                    dictionary['Canine'][canineCount].setName(row[1])
                    dictionary['Canine'][canineCount].setInventory(row[5], int(row[6]), float(row[7]))
                    canineCount += 1

                elif row[0] == 'Feline':
                    #Creates feline object in inventory based on csv attributes
                    dictionary['Feline'].append(Feline(row[2], float(row[3]), row[4]))
                    dictionary['Feline'][felineCount].setName(row[1])
                    dictionary['Feline'][felineCount].setInventory(row[5], int(row[6]), float(row[7]))
                    felineCount += 1

                elif row[0] == 'Snake':
                    #Creates snake object in inventory based on csv attributes
                    dictionary['Snake'].append(Snake(row[2], float(row[3]), row[4], bool(row[5]), row[6]))
                    dictionary['Snake'][snakeCount].setName(row[1])
                    dictionary['Snake'][snakeCount].setInventory(row[7], int(row[8]), float(row[9]))
                    snakeCount += 1

                elif row[0] == 'Lizard':
                    #Creates lizard object in inventory based on csv attributes
                    dictionary['Lizard'].append(Lizard(row[2], float(row[3]), row[4], row[5], bool(row[6]), bool(row[7])))
                    dictionary['Lizard'][lizardCount].setName(row[1])
                    dictionary['Lizard'][lizardCount].setInventory(row[8], int(row[9]), float(row[10]))
                    lizardCount += 1

                # Remove keys from dictionary if there are no pets inside
                copy_dict = dictionary.copy()

                for key, value in copy_dict.items():
                    if len(value) == 0:
                        dictionary.pop(key)
                        pets.remove(key)


def savePetstore():
    with open('PetStore.csv', 'w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)

        #Writes canine attributes into csv
        if 'Canine' in inventory:
            for pet in inventory['Canine']:
                csvWriter.writerow(['Canine', pet.getName(), pet.getSize(), pet.getWeight(), pet.getColor(),
                                    pet.inventory.getLocation(), pet.inventory.getQuantity(), pet.inventory.getPrice()])

        #Writes feline attributes into csv
        if 'Feline' in inventory:
            for pet in inventory['Feline']:
                csvWriter.writerow(['Feline', pet.getName(), pet.getSize(), pet.getWeight(), pet.getColor(),
                                    pet.inventory.getLocation(), pet.inventory.getQuantity(), pet.inventory.getPrice()])

        #Writes snake attributes into csv
        if 'Snake' in inventory:
            for pet in inventory['Snake']:
                csvWriter.writerow(['Snake', pet.getName(), pet.getSize(), pet.getWeight(), pet.getColor(),
                                    pet.isConstrictor(), pet.getFood(), pet.inventory.getLocation(),
                                    pet.inventory.getQuantity(), pet.inventory.getPrice()])

        #Writes lizard attributes into csv
        if 'Lizard' in inventory:
            for pet in inventory['Lizard']:
                csvWriter.writerow(['Lizard', pet.getName(), pet.getSize(), pet.getWeight(), pet.getColor(),
                                    pet.getHabitat(), pet.hasFrill(), pet.hasSpikes(), pet.inventory.getLocation(),
                                    pet.inventory.getQuantity(), pet.inventory.getPrice()])


#Defines set up store function
def setupStore():

    #Calls create functions for each type of inventory
    createCanine(inventory)
    createFeline(inventory)
    createSnake(inventory)
    createLizard(inventory)

    #Remove keys from dictionary if there are no pets inside
    copy_dict = inventory.copy()

    for key, value in copy_dict.items():
        if len(value) == 0:
            inventory.pop(key)
            pets.remove(key)


#Defines display inventory function
def displayInventory(dictionary):
    print('We offer the following pets')
    #Nested for loop to view pet inventory
    for i in range(len(dictionary)):
        print(f'{pets[i]}:')
        for j in range(len(dictionary[pets[i]])):
            print(f'\t{dictionary[pets[i]][j].getName()} count {dictionary[pets[i]][j].inventory.getQuantity()} cost '
                  f'${dictionary[pets[i]][j].inventory.getPrice():,.2f}.')


#Defines POS function
def POS(dictionary1, dictionary2):
    #Displays the categories of pets available for sale and asks user what pet they would like to buy
    print('What category would you like to sale: ')
    for idx, (key, value) in enumerate(dictionary2.items(), start=1):
        print(f"{idx}: {key}")
    typeOfPetSelling = int(input('What is being sold: '))
    typeOfPetSelling = pets[typeOfPetSelling - 1]

    for i in range(len(inventory[typeOfPetSelling])):
        print(f'{i + 1}: {inventory[typeOfPetSelling][i].getName()}')
    exactPet = int(input(f'What {typeOfPetSelling} are being sold: '))

    petQuantity = int(input(f'how many {inventory[typeOfPetSelling][exactPet - 1].getName()} are being sold: '))

    #Makes sure there are more or the same amount of pets available as there are being sold
    while dictionary2[typeOfPetSelling][exactPet - 1].inventory.getQuantity() < petQuantity:
        print(f'We dont have that many, try again')
        petQuantity = int(input(f'how many {inventory[typeOfPetSelling][exactPet - 1].getName()} are being sold: '))

    dictionary1[typeOfPetSelling] = {inventory[typeOfPetSelling][exactPet - 1]: petQuantity}


#Defines calculate tax function
def calculateTax(num):
    stateTax = 0.07
    federalTax = 0.10
    total = num + (stateTax * num) + (federalTax * num)
    print(f'{"State tax":>21}{" "*11}${stateTax:.2f}')
    print(f'{"Federal tax":>23}{" "*9}${federalTax:.2f}')
    print(f'{"Total due":>21}{" "*11}${total:,.2f}')

#Defines display receipt function
def displayReceipt(dictionary):
    print('Aggie Pet Store Bill of Sale')
    print()
    print('_' * 50)
    count = 1
    priceCount = 0
    #Nested loops to print out each item in dictionary

    for items in dictionary:
        for i, j in dictionary[items].items():
            print(
                f'{count}. {items:6}   {i.getName():7} ${i.inventory.getPrice():5.2f}  {j:2}  ${i.inventory.getPrice() * j:,.2f}')
            priceCount += i.inventory.getPrice() * j


    calculateTax(priceCount)
    print('_' * 50)


#Defines close pet store function
def closePetStore():
    print('Thank you for using the Aggie PetStore POS')
    print('Aggie Pride!')

#Call load petstore to either load in pet data or set up store
loadPetstore(inventory)


#Defines the menu
while True:
    print('A) Display Pets')
    print('B) Sale Pet')
    print('C) Total Sale')
    print('E) Exit')
    choice = input('Menu selection: ').upper()
    #Calls functions corresponding to each menu prompt
    if choice == 'E':
        savePetstore()
        closePetStore()
        break
    elif choice == 'A':
        displayInventory(inventory)
    elif choice == 'B':
        POS(billOfSale, inventory)
    elif choice == 'C':
        displayReceipt(billOfSale)