from plates import is_valid

def test_cond1():
    assert is_valid("CS50")
    assert not is_valid("C50")
    assert is_valid("AAAA")

def test_cond2():
    assert is_valid("CRED43")
    assert not is_valid("C")
    assert is_valid("AA")

def test_cond3_0():
    assert is_valid("ABC5")
    assert not is_valid("CS5T")
    assert not is_valid("AAAA0A")

def test_cond3_1():
    assert is_valid("CRF50")
    assert not is_valid("AAAA00")

def test_cond4():
    assert not is_valid("CS,50")
    assert not is_valid("C5(0)")
    assert not is_valid("AAA:)")
