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

### Bonus Features
1. Rock-Paper-Scissors-Spock-Lizard
2. Shorten input so player doesn't have to type the whole word for their choice
3. Keep score of the player's and computer's wins. When either the player or computer reaches three wins, the match is over, and the winning player becomes the grand winner.

## PEDAC

### INPUTS
user inputs: choice of rock, paper, scissors, spock, lizard
computer input: also choice of rock, paper, scissors, spock, lizard

### OUTPUTS

display each game winner
display # games won by player and computer
display match winner (best of 5)

### RULES

1. rock > scissors
2. paper > rock
3. scissors > paper
4. rock > lizard
5. lizard > spock
6. spock > scissors
7. scissors > lizard
8. lizard > paper
9. paper > spock
10. spock > rock
11. tie if both players choose same
12. shortened inputs:
* 'r' for 'rock'
* 'p' for 'paper'
* 'sc' for 'scissors'
* 'sp' for 'spock'
* 'l' for 'lizard'

### MENTAL MODEL
Ask user to input rock, paper, scissors, spock, lizard. Then computer selects random choice among rock, paper, scissors, spock, lizard. Compare user input to computer choice and select winner based on RPS rules. Keep track of number of wins for both player and computer. Game continues playing until either player or computer reaches 3 wins, then announce grand winner.  

### TEST CASES 

Handle situation if user & computer select same choice -- tie
No points for either player or computer for a tie

### DATA STRUCTURE

strings, dictionary for choices

### ALGORITHM
1. Initialize constant VALID_CHOICES to a dictionary mapping shortened inputs to rock, paper, scissors, spock, lizard. Dictionary keys are 'r', 'p', 'sc', 'sp', 'l' with corresponding values 'rock', 'paper', 'scissors', 'spock', 'lizard'
2. Define `prompt` function that prints f-string concatenating message w/prompt
3. Define `who_wins_game` function that chooses winner, two parameters with player choice & computer choice, 
use a series of if/elif statements to compare choices using VALID_CHOICES keys & determine winner, 
else tie if choices are same. Instead of printing winner, return winner or tie. 
4. Set `player_wins` and `computer_wins` to 0. These variables will be counters to keep track of # games won.
5. Enclose following code in `while True` loop: 
6. Ask user to input choice. Variable `player_choice` references input value.
7. While choice not in VALID_CHOICES, ask user for valid input.
8. Use random.choice function for the computer's choice among VALID_CHOICES. Variable `computer_choice` references return value.
9. Invoke `who_wins_game` with arguments of `player_choice` & `computer_choice`. Variable `game_winner` references return value if return value != 'tie'.
10. If `game_winner == 'player'` increment `player_wins` by 1, print you win. If `game_winner == 'computer'` increment `computer_wins` by 1 and print computer wins. Else print tie, neither game counter variable is incremented.
11. Print match score with f-string argument interpolating `player_wins` and `computer_wins`
12. If `player_wins == 3` print you win the match, break. Elif `computer_wins == 3` print computer wins, break

