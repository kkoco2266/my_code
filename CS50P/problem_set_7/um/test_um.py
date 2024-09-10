from um import count

def test_em1():
    assert count("Um umbrella") == 1
    assert count("um um um um") == 4

def test_um0():
    assert count("UMUM UM") == 1
    assert count("UM UMM       UM") == 2

def test_um1():
    assert count("Um uM ") == 2
