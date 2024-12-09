import csv
import os

    #Brings the file into the program
with open('wordle.csv', 'r')as file:
    #Puts the file in a variable
    csv_reader = csv.reader(file)
    #Turns the variable into a list
    wordAnswers = list(csv_reader)

#Creating a test list and a possible answer list seperate from the original to add a reset function
testList = []
possibleAnswers = wordAnswers

class Inputs:
    def __init__(self, letter, position, color):
        self.letter = letter
        self.position = position
        self.color = color        

#This list will contain all user inputs
userInputs = []

#This function turns the user inputs into an object and adds them to the user input list
def addInputs(letter, color, position):
    userInputs.append(Inputs(letter, int(position) - 1, color))

######################## THERE IS TONS OF OPTIMIZATION I COULD DO TO THIS FUNCTION BUT I DO NOT THINK IT MATTERS BECAUSE IT RUNS IN LESS THAN A SECOND ########################

def testInputs(TestList, AnswerList, inputs):
    #Sets the testlist to availible answers for optimization
    TestList = AnswerList 
    #Empties the answerlist before the tests are ran on the testlist and words are added to the answer list
    AnswerList = [] 
    for word in TestList:
        testSubject = word[0] #Index the test subject
        #Track all successful checks made on a word
        successCheck = 0 
        #Track the total number of checks made on a word
        checkCount = 0 
        for item in inputs:
            #Initiates the check process for each user input
            checkCount += 1

            #For each letter checked, if it is successful the success count will increase with the check count
            if item.color == 'green':
                if testSubject[item.position] == item.letter: 
                    successCheck += 1 
            elif item.color == 'yellow':
                if item.letter in testSubject and testSubject[item.position] != item.letter: 
                    successCheck += 1 
            elif item.color == 'gray':
                if item.letter not in testSubject:
                    successCheck += 1 
        #If the success count is equal to the total check count then the test word is added to the possible answer list
        if successCheck == checkCount:
            AnswerList.append(testSubject) 
    print(AnswerList)

######################## THERE IS TONS OF OPTIMIZATION I COULD DO TO THIS FUNCTION BUT I DO NOT THINK IT MATTERS BECAUSE IT RUNS IN LESS THAN A SECOND ########################

#INPUT VALIDATION FUNCTIONS
def is_valid_letter(letter):
    return len(letter) == 1 and letter.isalpha()

def is_valid_color(color):
    return color.lower() in ['gray', 'green', 'yellow']

def is_valid_position(position):
    return position.isdigit() and 1 <= int(position) <= 5

os.system('cls')

while True:
    while True:
        try:
            howManyLetters = int(input('How many letters would you like to enter? \n'))
            if howManyLetters > 0 and howManyLetters <= 5:
                break
            else:
             print("Please enter a positive number. \n")
        except ValueError:
            print("Invalid input. Please enter a whole number. \n")
    quack = 0
    while quack < howManyLetters:
        while True:
            userLetter = input('Letter \n').strip().lower()
            if is_valid_letter(userLetter):
                break
            else:
                print("Invalid letter. Please enter a single lowercase alphabet character. \n")
        while True:
            userColor = input('Color \n').strip().lower()
            if is_valid_color(userColor):
                break
            else:
                print("Invalid color. Please enter 'gray' 'green' or 'yellow'. \n")
        while True:
            userPosition = input('Position \n').strip()
            if is_valid_position(userPosition):
                userPosition = int(userPosition)  
                break
            else:
                print("Invalid position. Please enter a number between 1 and 5. \n")
        addInputs(userLetter, userColor, userPosition)
        quack += 1
        os.system('cls')
    testInputs(testList, possibleAnswers, userInputs)
    while True:
        stopReset = input('stop or continue? \n').strip().lower()
        if stopReset in ['stop', 'continue']:
            break
        else:
            print('Invalid input. Please enter "stop" or "continue."')
    if stopReset == 'stop':
        break
