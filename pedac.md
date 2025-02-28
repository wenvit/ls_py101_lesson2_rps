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

rock > scissors
paper > rock
scissors > paper

### MENTAL MODEL
Ask user to input rock, paper, or scissors. Then computer selects random choice among rock, paper, or scissors. Compare user input to computer choice and select winner based on RPS rules. Ask user if they'd like to continue game.

### TEST CASES 

Handle situation if user & computer select same choice -- do over

### DATA STRUCTURE

strings, lists for choices

### ALGORITHM
1. prompt function
2. ask user to input choice
3. while choice not in ['rock', 'paper', 'scissors']
   ask user for valid input
4. use random.choice function for the computer's choice among
   ['rock', 'paper', 'scissors']
5. user a series of if/elif statements to compare user & computer 
   choices to determine & print winner, if choices are equal, 
   continue next iteration of while loop
6. ask user if she wants to play again, if no break

