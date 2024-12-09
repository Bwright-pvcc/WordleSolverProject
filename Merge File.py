import csv
import os
from nicegui import ui 

    #Brings the file into the program
with open('wordle.csv', 'r')as file:
    #Puts the file in a variable
    csv_reader = csv.reader(file)
    #Turns the variable into a list
    wordAnswers = list(csv_reader)

# This is the user input 
class UIInput(ui.input): 
    # Not fully sure what this does but it works 
     def __init__(self, B1, *args, **kwargs, ) -> None:
        super().__init__(*args, **kwargs)
        # When the enter key is pressed it runs the change function
        self.on('change', self.change)
        self.B1 = B1
    
     def change(self, selflist) -> None: 
        # Sets the value to the current value 
        # Not sure if this is fully nessisary but I'm not changing it 
        self.value = self.value
        # Checking the correct Input Length 
        if len(self.value) == 5:
            selflist = list(self.value)
            # Makes a Group of 5 Buttons out of the list of the user's input 
            with ui.button_group():
                B = ToggleButton(selflist[0])
                ToggleButton(selflist[1])
                ToggleButton(selflist[2])
                ToggleButton(selflist[3])
                ToggleButton(selflist[4])
            self.B1 = B._state
            ToggleButton(self.B1)
        # Updates the UI to reflect the changes 
        # This is what allows the input to update after the code has run 
        super().update()
         
 

# This is the Specific Button that can change it's color 
class ToggleButton(ui.button):

    def __init__(self, *args, **kwargs,) -> None:
        super().__init__(*args, **kwargs)
        #Default State is 1
        self._state = 1
        #When the button is clicked run the Toggle Function
        self.on('click', self.toggle)

    def toggle(self) -> None:
        """Toggle the button state."""
        # Increment the state
        self._state = self._state + 1
        # If the state is 4 loop back to 1 
        if (self._state == 4):
            self._state = 1
        # Run the update function 
        self.update()

    def update(self) -> None:
        #Changes the color depending on the state
        self.props(f'color={"grey" if self._state == 1 else ""}')
        self.props(f'color={"yellow" if self._state == 2 else ""}')
        self.props(f'color={"green" if self._state == 3 else ""}')
        #This is what allows the button to update after the code has run 
        super().update()


#Creating a test list and a possible answer list seperate from the original to add a reset function
testList = []
possibleAnswers = wordAnswers


class SubmitButton(ui.button): 
    def __init__(self, *args, **kwargs,) -> None:
        super().__init__(*args, **kwargs)
        self.on('click', self.toggle)
    
    def toggle(self) -> None: 
        ui.button(UIInput.B1)
        self.update()


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


os.system('cls')

UIInput(7)
SubmitButton()

# Do the UI
ui.run()
