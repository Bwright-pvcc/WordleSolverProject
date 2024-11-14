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
            position = int(row[2].strip())
            rowCount += 1

            if color == 'Green':
                if testSubject[position] == letter: #If the color is green and the letter in the position of the word is the same as the green user letter
                    successCheck += 1 #It will increase the successful checks by 1
            elif color == 'Yellow':
                if letter in testSubject and testSubject[position] != letter: #If the word contains the letter and the letter is not in the same position as the yellow user letter
                    successCheck += 1 #It will increase the successful checks by 1
            elif color == 'Gray':
                if letter not in testSubject: #If the word does not contain the gray user letter
                    successCheck += 1 #It will increase the successful checks by 1
        if successCheck == rowCount:
            AnswerList.append(testSubject) #If each check was successful then the word is added to the list
    print(AnswerList)

#Placeholder inputs to test multiple inputs on the table
quack = 0
while quack < 3:
    userLetter = input('letter \n')
    userColor = input('color \n')
    userPosition = input('position \n')
    addInputs(userLetter, userColor, userPosition)
    quack += 1

testInputs(testList, possibleAnswers, lettersTable)

print(lettersTable)
