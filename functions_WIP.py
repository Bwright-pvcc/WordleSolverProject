import csv
from prettytable import PrettyTable

#Brings the file into the program
with open('wordle.csv', 'r')as file:
    #Puts the file in a variable
    csv_reader = csv.reader(file)
    #Turns the variable into a list
    wordAnswers = list(csv_reader)

#Gonna need these for later
testList = []
possibleAnswers = []


#Creates the Table
lettersTable = PrettyTable()

#Adds Headers to the table
lettersTable.field_names = ["Letter","Color","Position"]

#Function to add user inputs to the table that will be used for storing values for checking validity of words on the list.
def addInputs(letter, color, position):
    lettersTable.add_row([letter, color, position])

#Placeholder inputs while I wait for BEN to finish
userLetter = input('letter \n')
userColor = input('color \n')
userPosition = input('position \n')

#Runs the function on the user inputs.
addInputs(userLetter, userColor, userPosition)

print(lettersTable)
