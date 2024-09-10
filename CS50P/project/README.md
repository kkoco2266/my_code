# TIC-TAC-TOE GAME
#### Video Demo: https://youtu.be/lFFuQ4LUOuw
#### Description:

#### *The project in action*
My project is a tic-tac-toe game. The program takes in no command-line arguments. Once you run the program, a message saying `These are the positions on the board` is displayed along with a 3x3 grid filled with numbers 1 to 9 which represent the spots on the board. Another message saying `Player 1 uses X and Player 2 uses O` is also displayed. An empty board is then displayed right after the `This is your board` message. The program then tells us that `It is Player 1's turn` and the user is prompted to give an input following the message `Input number that corresponds to the spot you would like to play at: `.

The user must then input a number from 1 to 9 depending on the preferred spot to play for player 1. Once the number is inputted, an X will appear at the spot chosen. The message `This is your board` reappears followed by your board which includes the X at the position player 1 chose. The program then informs you that `It is Player 2's turn` and the user is prompted to give an input following the message `Input number that corresponds to the spot you would like to play at: `.

If any other input apart from the digits 1 to 9 are inputted, the program would display the message `The number you inputted is invalid` and repromt the user to give an input with the same message as before. This will happen till a correct input has been given. However if a number is inputted but the spot has already been played at, a message saying `The spot you chose is already taken, pick another one` followed by a reprompt to give an input with the same message as before.

Once a player wins, the program displays `Player 1 wins!!!` or `Player 2 wins!!!` depending on who won and the program ends right after.

If the game is going to end in a draw, the program will predict it before the last move is played and say `It is a draw !!!`.


#### *Into the file* `project.py`
I began the project by importing the `tabulate` library (which I installed via pip) and the `copy` library. The `tabulate` library was used to draw the playing board and the `copy` library was used to make deep copies which was very important later. I could have manually drawn the board using symbols or even created a function for that but why bother if there is a library that can do that for you.

I then created two custom exceptions (ie. `OccupiedError` and `WrongInputError`). I could have achieved the same goal by using some of the built-in exceptions but I wanted to try something new for a change.

I went on to create a class called `Board()` which takes no arguments at creation and has two attributes `self.board` which is a nested list filled with numbers 1 to 9 that represents the play area and `self.empty_spaces` which is an `int` that represents number of empty spots. These are defined in `__init__`. I also defined `__str__` such that when a `Board()` is passed into a print function, it prints the board without the numbers . The class also has a `self.fill()` function which takes two arguments, the character to be played (ie. `X` or `O`) and the position it should be played (ie. a number from 1 to 9). This function replaces on the board whatever number was passed into it with the character passed into it.. It raises an `OccupiedError` if the spot you want to play is already taken and a `WrongInputError` if the character passed into it is not a `X` or `O`. Raising a `WrongInputError` was actually useless because of how I designed my main function but I left it there.

I could have made a variable to represent the board but then I would have to make it global since it would be passed through many functions so I decided to rather make a class object to solve all my problems.

I then implemented a function called `the_player_of` which takes a character (ie. `X` or `O`) as an argument and returns the player whose character was passed into it (ie `player 1` or `player 2`).

I also implemented a function called `won()` which takes a `Board()` object as an argument. It returns `True` and prints `player 1 wins!!!` or `player 2 wins!!!` if a player wins and it only returns `False` if no one has won yet.

There is also a function called `draw` which takes a `Board()` object as an argument. It first checks how many empty spaces are left on the board. If there is more than one space left, the function returns `False`. However if there is exactly one space left, it then passes the board into the `won()` function. If this returns `False` then it prints `"It is a draw !!!` and returns `True`. If not, it still returns `True`.

The `main()` function creates a `Board()` object called `game_board`, creates a variable `continue_game` and sets it to `True`. It then creates a while loop with `continue_game` as the condition. In the loop, a board with numbers is printed first to let the players know which number corresponds to each position. It then uses a while loop with try and except in order to catch any errors in the players' inputs. `continue_game = not won(game_board) and not draw(game_board)` is coded at the end of the while loop. This ensures `continue_game` is set to `False` if someone wins or draws, thereby breaking out of the the while loop

#### *Into the file* `test_project.py`
This file imports `the_player_of` , `won` and `draw` functions and also the `Board` object class. It goes ahead to define three functions that test the three functions that were imported each with the prefix `test_` and the name of the function it tests.

#### *Into the file* `requirements.txt`
This file contains the only pip installed library used in my project which is `tabulate`
