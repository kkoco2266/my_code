from numb3rs import validate

def test_digits():
    assert validate("1.0.4.9")
    assert validate("4.9.5.3")
    assert validate("2.9.6.7")
    assert validate("2.8.6.4")
def test_tens():
    assert validate("10.99.15.9")
    assert validate("20.14.95.0")
    assert validate("29.28.88.5")
    assert validate("5.10.15.20")

def test_hundreds():
    assert validate("26.90.100.150")
    assert validate("250.90.106.209")
    assert validate("208.160.178.200")
    assert not validate("250.1000.30.40")
    assert not validate("255.70.900.30")

def test_wrongs():
    for i in range(256, 1000):
        i = str(i)
        assert not validate(f"{i}.{i}.{i}.{i}")

def test_etc():
    assert not validate("cat")
    assert not validate("200.0.0")
    assert not validate("2000")
