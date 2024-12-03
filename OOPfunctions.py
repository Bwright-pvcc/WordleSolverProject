###########################################  NOT SURE IF I WILL USE THESE OR NOT, THE PRETTY TABLE FUNCIONS WORK PROPERLY. I WANT TO LEARN OOP AND WANT TO TRY AND GET THESE TO WORK TO, IT SHOULD ALSO RUN SMOOTHER THAN PRETTY TABLE BUT WE'RE TALKING LIKE MILLISECONDS SAVED  ########################################### 

import csv
import os

    #Brings the file into the program
with open('wordle.csv', 'r')as file:
    #Puts the file in a variable
    csv_reader = csv.reader(file)
    #Turns the variable into a list
    wordAnswers = list(csv_reader)

 #Gonna need these for later
testList = []
possibleAnswers = wordAnswers

class Inputs:
    def __init__(self, letter, position, color):
        self.letter = letter
        self.position = position
        self.color = color        

userInputs = []

#Function to add user inputs to the table that will be used for storing values for checking validity of words on the list.
def addInputs(letter, color, position):
    userInputs.append(Inputs(letter, int(position) - 1, color))

#The Holy Grail, This function is ran on every word in the entire list of Test Subjects and each letter is ran on every word.
def testInputs(TestList, AnswerList, inputs):
    TestList = AnswerList #Sets the testlist to availible answers for optimization
    AnswerList = [] #Empties the answerlist before the tests are ran on the testlist and words are added to the answer list
    for word in TestList:
        testSubject = word[0] #Index the test subject
        successCheck = 0 #Variable to track successful checks
        checkCount = 0 #Variable to track rows iterated through
        for item in inputs: #Index the table and remove the headers
            checkCount += 1

            if item.color == 'green':
                if testSubject[item.position] == item.letter: #If the color is green and the letter in the position of the word is the same as the green user letter
                    successCheck += 1 #It will increase the successful checks by 1
            elif item.color == 'yellow':
                if item.letter in testSubject and testSubject[item.position] != item.letter: #If the word contains the letter and the letter is not in the same position as the yellow user letter
                    successCheck += 1 #It will increase the successful checks by 1
            elif item.color == 'gray':
                if item.letter not in testSubject: #If the word does not contain the gray user letter
                    successCheck += 1 #It will increase the successful checks by 1
        if successCheck == checkCount:
            AnswerList.append(testSubject) #If each check was successful then the word is added to the list
    print(AnswerList)

#INPUT VALIDATION FUNCTIONS
def is_valid_letter(letter):
    return len(letter) == 1 and letter.isalpha()

def is_valid_color(color):
    return color.lower() in ['gray', 'green', 'yellow']

def is_valid_position(position):
    return position.isdigit() and 1 <= int(position) <= 5

os.system('cls')

#I'm just gonna make input validation and turn this thang in whenever
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
                userPosition = int(userPosition)  # Convert to int for processing
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
