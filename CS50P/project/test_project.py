from project import the_player_of , won , draw , Board
import pytest


def test_the_player_of():
    assert the_player_of("X") == "player 1"
    assert the_player_of("O") == "player 2"
    with pytest.raises(ValueError):
        assert the_player_of("cat")
    with pytest.raises(ValueError):
        assert the_player_of(5)
    with pytest.raises(ValueError):
        assert the_player_of('x')
    assert the_player_of("X") == "player 1"


def test_won():
    bord = Board()
    assert not won(bord)
    bord.board = [['X', 'O', '3'], ['X', 'X', 'O'], ['X', '8', 'O']]
    assert won(bord)
    bord.board = [['X', '2', 'O'], ['4', 'X', 'O'], ['X', '8', 'O']]
    assert won(bord)
    bord.board = [['X', 'O', 'O'], ['O', 'X', 'X'], ['7', 'X', 'O']]
    assert not won(bord)


def test_draw():
    bord = Board()
    assert not draw(bord)
    bord.board = [['X', 'O', 'O'], ['O', 'X', 'X'], ['7', 'X', 'O']]
    assert draw(bord)
    bord.board = [['X', '2', 'O'], ['4', 'X', 'O'], ['X', '8', 'O']]
    assert not won(bord)
def test_Board():
    bord = Board()
    assert bord.empty_spaces == 9
