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
