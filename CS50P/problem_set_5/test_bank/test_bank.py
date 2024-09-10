from bank import value

def test_hello():
    assert value('Hello') == 0
    assert value('hello, sir') == 0

def test_h():
    assert value('Hi') == 20
    assert value('hey') == 20
    assert value('Hudson!') == 20

def test_no_h():
    assert value('good morning, sir') == 100
    assert value('what do you want?') == 100
    assert value('yo bro') == 100
