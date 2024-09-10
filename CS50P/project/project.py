from tabulate import tabulate
import copy


class OccupiedError(BaseException):
    def __init__(self, message=None):
        self.message = message
        super().__init__(message)


class WrongInputError(BaseException):
    def __init__(self, message=None):
        self.message = message
        super().__init__(message)


class Board():
    def __init__(self) -> None:
        self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.empty_spaces = 9

    def __str__(self):
        list_of_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        bordcopy = copy.deepcopy(self.board)
        for i in range(3):
            bordcopy[i] = [' ' if spot in list_of_nums else spot for spot in bordcopy[i]]
        return tabulate(bordcopy, tablefmt="grid")

    def fill(self, character: str, position: str):
        if character != 'X' and character != 'O':
            raise WrongInputError
        elif not position in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            raise ZeroDivisionError
        board_copy = copy.deepcopy(self.board)
        for i in range(3):
            self.board[i] = [num if num != position else character for num in self.board[i]]
        if self.board == board_copy:
            raise OccupiedError
        else:
            self.empty_spaces -= 1

# The board looks like this
#   1|2|3
#   4|5|6
#   7|8|9


def main():
    game_board = Board()
    continue_game = True
    new_game = True
    while continue_game:
        spots_available = game_board.empty_spaces
        if new_game:
            print(
                f"""\nThese are the positions on the board\n{tabulate([['1','2','3'] , ['4','5','6'] , ['7','8','9']], tablefmt='grid')}""")
            print("\nPlayer 1 uses X and Player 2 uses O")
            print(f"""\nThis is your board\n{game_board}""")
            new_game = False
        if spots_available % 2 == 1:
            print("\nIt is Player 1's turn\n")
            while True:
                try:
                    pos = input(
                        "Input number that corresponds to the spot you would like to play at: ").strip()
                    game_board.fill("X", pos)
                    break
                except OccupiedError:
                    print("The spot you chose is already taken, pick another one")
                    pass
                except ZeroDivisionError:
                    print("The number you inputted is invalid")
            print(f"""This is your board\n{game_board}""")
        else:
            print("\nIt is Player 2's turn\n")
            while True:
                try:
                    pos = input(
                        "Input number that corresponds to the spot you would like to play at: ").strip()
                    game_board.fill("O", pos)
                    break
                except OccupiedError:
                    print("The spot you chose is already taken, pick another one")
                    pass
                except ZeroDivisionError:
                    print("The number you inputted is invalid")
            print(f"""This is your board\n{game_board}""")

        continue_game = not won(game_board) and not draw(game_board)


def the_player_of(character: str):
    if character == "X":
        return "player 1"
    elif character == "O":
        return "player 2"
    else:
        raise ValueError("Wrong Character Passed into the_player_of function")


def won(bord):
    kk = copy.deepcopy(bord.board)
    p1 = kk[0][0]
    p2 = kk[0][1]
    p3 = kk[0][2]
    p4 = kk[1][0]
    p5 = kk[1][1]
    p6 = kk[1][2]
    p7 = kk[2][0]
    p8 = kk[2][1]
    p9 = kk[2][2]

    if p1 == p2 == p3:
        print(f"{the_player_of(p1).title()} wins!!!")
        return True
    elif p4 == p5 == p6:
        print(f"{the_player_of(p4).title()} wins!!!")
        return True
    elif p7 == p8 == p9:
        print(f"{the_player_of(p7).title()} wins!!!")
        return True
    elif p1 == p4 == p7:
        print(f"{the_player_of(p1).title()} wins!!!")
        return True
    elif p2 == p5 == p8:
        print(f"{the_player_of(p2).title()} wins!!!")
        return True
    elif p3 == p6 == p9:
        print(f"{the_player_of(p3).title()} wins!!!")
        return True
    elif p1 == p5 == p9:
        print(f"{the_player_of(p1).title()} wins!!!")
        return True
    elif p3 == p5 == p7:
        print(f"{the_player_of(p3).title()} wins!!!")
        return True
    else:
        return False


def draw(board):
    board_copy = Board()
    board_copy.board = copy.deepcopy(board.board)
    spaces = board.empty_spaces
    if spaces == 1:
        position = [num for row in board_copy.board for num in row if num != "X" and num != "O"]
        board_copy.fill("X", *position)
        if not won(board_copy):
            print("It is a draw !!!")
        return True
    else:
        return False


if __name__ == "__main__":
    main()
