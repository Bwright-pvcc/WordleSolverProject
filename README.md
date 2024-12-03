# WordleSolverProject

#### Problem: 
Solving the Wordle takes time and mental energy. 

#### Goal: 
Create a program that solves the daily Wordle. 

#### Process: 
Feed the program my Wordle letters and it will show a list of possible answers remaining
User will Input each letter and then input whether that letter is yellow green or gray 
Potentially create a User input system that will make inputting letters much easier 

#### Analysis: 
Letters will have a default state of black 
The user inputs a letter, its position, and its state  
The program then iterate through the list of possible wordle answers and removes words that don’t match then returns the remaining list 
Each time the user is prompted to input a letter they will also be prompted with (INPUT EXIT TO LEAVE) in order to close the program.

#### Challenges: 
The input process is going to be very tedious so if we have time we’ll make a cleaner input system
If someone is playing a different version of Wordle the list will need to be replaced. Could potentially store the list in a separate variable and add another input for the user to simply restart the program.

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
#### PSA FROM GREG
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
#### The One Issue (I think)
The test list will not contain any words when it is originally used so the very first time the program is ran it will have to use the original list of words. This can be solved via a while loop with the first test of user inputs being done through the words list and then embedding another while loop inside the first while loop with the "testWords" function inside that can then be ran as many times as the user wants.







#### Final implementation by Greg

So I originally had tried to remove bad words from a list inside of a loop (that was a really dumb idea in hindsight) and then changed over to adding good words to a list which was really smart. But I had to figure out a way to store three different user inputs together. My first solution was to use PrettyTables, which worked fantastic, but I didn't want to have to deal with the logistics of importing something new if I ever used this program on a different computer. So I converted the code that was 100% functional with PrettyTables over to Object-Oriented code. At first I had tried rewriting the whole thing (again a really dumb idea) and then realized it was WAYYYY easier to just take all of the parts that had PrettyTables and just convert it to a class, a list, and objects. 

Now the algorithm works by obtaining user inputs, putting them inside and object, putting the object in a list of user inputs, setting a test list to all the possible answers based on the tests ran with user inputs, emptying the possible answer list, running tests based on user inputs, and if each test is successful on each word then the word is added to the list of possile answers. After each word is test the possible answer list is shown to the user who can continue to use the program as needed.
