###########################################  NOT SURE IF I WILL USE THESE OR NOT, THE PRETTY TABLE FUNCIONS WORK PROPERLY. I WANT TO LEARN OOP AND WANT TO TRY AND GET THESE TO WORK TO, IT SHOULD ALSO RUN SMOOTHER THAN PRETTY TABLE BUT WE'RE TALKING LIKE MILLISECONDS SAVED  ########################################### 

import csv

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
    def __init__(self, char='', position=0, color=''):
        self.char = char
        self.position = position
        self.color = color

def testInputs(TestList, Answerlist, lettersFunc):
    TestList = Answerlist
    AnswerList = []
    for word in TestList:
         word = word[0] #Index the test subject
         successCheck = 0
         testCount = 0
         for i in range (len(lettersFunc)):
            letter = lettersFunc[i]
            if letter.color == "Green":
                if letter.char in word:
                    if word.find(letter.char) == letter.position:
                        successCheck += 1
            elif letter.color == "Yellow":
                if letter.char in word:
                    if word.find(letter.char) != letter.position:
                        successCheck += 1
            elif letter.color == "Gray":
                if letter.char not in word:
                    successCheck += 1
            testCount += 1
         if testCount == successCheck:
            AnswerList.append(word)
    print(AnswerList)

def main():

    letters = []

    #Placeholder inputs to test multiple inputs on the table
    quack = True
    while quack:
        letter = input('letter \n')
        position = input('position \n')
        color = input('color \n')
        letters.append(Inputs(letter,int(position) - 1, color))
        stop = input('You want to stop \n')
        if stop == 'y':
            break
        else:
            quack = True
    testInputs(testList, possibleAnswers, letters)

main()
