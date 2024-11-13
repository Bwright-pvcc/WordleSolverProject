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
        for row in Table.rows: #Index the table and remove the headers
            letter = row[0]
            color = row[1].strip()
            position = int(row[2].strip())
            
            if color == 'Green':
                if testSubject[position] == letter: #If the color is green and the letter in the position of the word is the same as the green user letter
                    AnswerList.append(testSubject) #It will add the word to the list of possible answers
            elif color == 'Yellow':
                if letter in testSubject and testSubject[position] != letter: #If the word contains the letter and the letter is not in the same position as the yellow user letter
                    AnswerList.append(testSubject) #It will add the word to the list of possible answers
            elif color == 'Gray':
                if letter not in testSubject: #If the word does not contain the gray user letter
                    AnswerList.append(testSubject) #It will add the word to a list of possible answers
    print(AnswerList)

#Placeholder inputs while I wait for BEN to finish
userLetter = input('letter \n')
userColor = input('color \n')
userPosition = input('position \n')

#Runs the function on the user inputs.
addInputs(userLetter, userColor, userPosition)

testInputs(testList, possibleAnswers, lettersTable)

print(lettersTable)
