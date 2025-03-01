## Problem statement

In this assignment, we'll build a Rock Paper Scissors game. Rock Paper Scissors is a simple game played between two opponents. Both opponents choose an item from rock, paper, or scissors. The winner is decided according to the following rules:

If player a chooses rock and player b chooses scissors, player a wins.
If player a chooses paper and player b chooses rock, player a wins.
If player a chooses scissors and player b chooses paper, player a wins.
If both players choose the same item, neither player wins. It's a tie.
Our version of the game lets the user play against the computer. The game flow should go like this:

The user makes a choice.
The computer makes a choice.
The winner is displayed.

## PEDAC

### INPUTS
user inputs: choice of rock, paper, scissors
computer input: also choice of rock, paper, scissors

### OUTPUTS

display winner

### RULES

1. rock > scissors
2. paper > rock
3. scissors > paper
4. tie if both players choose same

### MENTAL MODEL
Ask user to input rock, paper, or scissors. Then computer selects random choice among rock, paper, or scissors. Compare user input to computer choice and select winner based on RPS rules. Ask user if they'd like to continue game.

### TEST CASES 

Handle situation if user & computer select same choice -- tie

### DATA STRUCTURE

strings, lists for choices

### ALGORITHM
1. define prompt function
2. define function that chooses winner - use a series of 
if/elif statements to compare choices & determine winner, 
else tie if choices are same
3. ask user to input choice
4. while choice not in ['rock', 'paper', 'scissors']
ask user for valid input
5. use random.choice function for the computer's choice among
['rock', 'paper', 'scissors']
6. ask user if she wants to play again, if no break

