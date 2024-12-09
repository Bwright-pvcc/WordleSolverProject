# WordleSolverProject (By: Greg and Ben) 

#### Problem: 
Solving the Wordle takes time and mental energy. 

#### Goal: 
Create a program that solves the daily Wordle (and looks good doing it) 

#### Process: 
Feed the program Wordle letters and it will show a list of possible answers remaining
User will input each letter and then input whether that letter is yellow green or gray 
Create a User input system that will make inputting letters much easier 

#### Analysis: 
Letters will have a default state of black
The user inputs a word, which is split into a letter and it's position, and the state of each letter  
The program then iterate through the list of possible wordle answers and removes words that don’t match then returns the remaining list 
Each time the user is prompted to input a letter they will also be prompted with (INPUT EXIT TO LEAVE) in order to close the program.

#### Challenges: 
If someone is playing a different version of Wordle the list will need to be replaced. Could potentially store the list in a separate variable and add another input for the user to simply restart the program.

Integrating Greg's code (The Algorithm) and Ben's code (The UI) was a pain because NiceGUI was difficult and, in order to update to user inputs, had to be interfaced with in a very particular way. 

#### The Algorithm (Pseudo-Code) 
These functions are the centerpiece of the entire program and one of them will be run for each input the user gives then responding with the remaining list of words.

```
words = (file of list of Wordle answers)
define greenLetter(letter, position)
if letter == Green:
	for word in words:
(Something here to turn each word into 5 different strings to iterate through)
		if position != letter
			remove word from words
define yellowLetter(letter, position)
if letter == Yellow:
	for word in words:
		(something here to turn each word into 5 different strings to iterate through)
		if position == letter
		remove word from words
define grayLetter(letter)
if letter == Gray
	for word in words:
	(something here to turn each word into 5 different strings to iterate through)
	if word contains letter
		remove word from words
```
#### Updated Pseudo-Code
This is a new edit to the algorithm. I am scrapping the old idea for a new one.
```
words = (file of list of Wordle Answers)
testList = (list of words to test)
possibleAnswers = (list of possible answers shown to the user)

define testWords(listTesting, listAnswers, UserInputs)
	listTesting = listAnswers
	listAnswers = []
	testUserInputFunction(listTesting, UserInuts)
	(THIS FUNCTION WILL ADD ALL VALID WORDS TO THE "listAnswers" LIST)
```
#### Potential Issues
The test list will not contain any words when it is originally used so the very first time the program is ran it will have to use the original list of words. This can be solved via a while loop with the first test of user inputs being done through the words list and then embedding another while loop inside the first while loop with the "testWords" function inside that can then be ran as many times as the user wants.

#### Final Algorithm by Greg

So I originally had tried to remove bad words from a list inside of a loop (that was a really dumb idea in hindsight) and then changed over to adding good words to a list which was really smart. But I had to figure out a way to store three different user inputs together. My first solution was to use PrettyTables, which worked fantastic, but I didn't want to have to deal with the logistics of importing something new if I ever used this program on a different computer. So I converted the code that was 100% functional with PrettyTables over to Object-Oriented code. At first I had tried rewriting the whole thing (again a really dumb idea) and then realized it was WAYYYY easier to just take all of the parts that had PrettyTables and just convert it to a class, a list, and objects. 

Now the algorithm works by obtaining user inputs, putting them inside an object, putting the object in a list of user inputs, setting a test list to all the possible answers based on the tests ran with user inputs, emptying the possible answer list, running tests based on user inputs, and if each test is successful on each word then the word is added to the list of possile answers. After each word is test the possible answer list is shown to the user who can continue to use the program as needed.

#### Final UI by Ben 

Because the User Input was going to be such a pain espically for people unfamilar with code, which is the majority of people, I used NiceGUI to create user friendly and clean UI. You will need to install NiceGUI first but this is a simple process. From there the user only needs to run the code and interact with the website created by it. 

The code is very simple. It creates a user input box that updates whenever the user makes a "change" in this case pressing the enter key. When the user enters a five character input it creates a series of boxes that can be toggeled to set their state, and a submit button which runs The Algorithm. The word boxes modify the color of the letters in the list created by the algorithm. I could not figure out how to restart the program so you have to do it manually, but I added a helpful reminder box. 

#### The Test Documents

* Main: Ben's finished UI (Unmerged)
* Mergefile: Ben's first attempt at merging OOPCode and Main
* Test: An early example of a user input controlling the text of a button
* Holding File: A slightly later example of the UI using refresh to constantly update 
* OOPFunctions: Greg's finished algorithm
* functions_WIP: An updated version of Greg's finished algorithm with tables that didn't end up getting used 

