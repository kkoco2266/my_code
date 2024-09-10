from seasons import day_to_min
import inflect, pytest
p = inflect.engine()

def test_output():
    assert day_to_min(50) == p.number_to_words(50*24*60, andword="")
    assert day_to_min(500) == p.number_to_words(500*24*60, andword="")
    assert day_to_min(4) == p.number_to_words(4*24*60, andword="")

def test_input():
    assert day_to_min('forty') == 'zero'
    assert day_to_min('cat') == 'zero'
    assert day_to_min('dog') == 'zero'
