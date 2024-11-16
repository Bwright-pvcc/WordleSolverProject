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
possibleAnswers = wordAnswers

lettersTable = PrettyTable() #Creates the Table

    #Adds Headers to the table
lettersTable.field_names = ["Letter","Color","Position"]

#Function to add user inputs to the table that will be used for storing values for checking validity of words on the list.
def addInputs(letter, color, position):
    lettersTable.add_row([letter, color, position])

#The Holy Grail, This function is ran on every word in the entire list of Test Subjects and each letter is ran on every word.
def testInputs(TestList, AnswerList, Table):
    TestList = AnswerList #Sets the testlist to availible answers for optimization
    AnswerList = [] #Empties the answerlist before the tests are ran on the testlist and words are added to the answer list
    for word in TestList:
        testSubject = word[0] #Index the test subject
        successCheck = 0 #Variable to track successful checks
        rowCount = 0 #Variable to track rows iterated through
        for row in Table.rows: #Index the table and remove the headers
            letter = row[0]
            color = row[1].strip()
            position = int(row[2])
            rowCount += 1

            if color == 'green':
                if testSubject[position] == letter: #If the color is green and the letter in the position of the word is the same as the green user letter
                    successCheck += 1 #It will increase the successful checks by 1
            elif color == 'yellow':
                if letter in testSubject and testSubject[position] != letter: #If the word contains the letter and the letter is not in the same position as the yellow user letter
                    successCheck += 1 #It will increase the successful checks by 1
            elif color == 'gray':
                if letter not in testSubject: #If the word does not contain the gray user letter
                    successCheck += 1 #It will increase the successful checks by 1
        if successCheck == rowCount:
            AnswerList.append(testSubject) #If each check was successful then the word is added to the list
    print(AnswerList)

#INPUT VALIDATION FUNCTIONS
def is_valid_letter(letter):
    return len(letter) == 1 and letter.isalpha()

def is_valid_color(color):
    return color.lower() in ['gray', 'green', 'yellow']

def is_valid_position(position):
    return position.isdigit() and 1 <= int(position) <= 5

#I'm just gonna make input validation and turn this thang in whenever
while True:
    while True:
        try:
            howManyLetters = int(input('How many letters would you like to enter? \n'))
            if howManyLetters > 0:
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
        addInputs(userLetter, userColor, (userPosition - 1))
        quack += 1
    testInputs(testList, possibleAnswers, lettersTable)
    print(lettersTable)
    while True:
        stopReset = input('stop or continue? \n').strip().lower()
        if stopReset in ['stop', 'continue']:
            break
        else:
            print('Invalid input. Please enter "stop" or "continue."')
    if stopReset == 'stop':
        break
