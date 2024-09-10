from jar import Jar
import pytest


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.capacity = -1
    with pytest.raises(ValueError):
        jar.size = -5

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(20)
    jar.deposit(15)
    assert jar.size == 15
    jar.deposit(4)
    assert jar.size == 19
    with pytest.raises(ValueError):
        jar.deposit(5)

def test_withdraw():
    jar = Jar(15)
    jar.deposit(15)
    jar.withdraw(12)
    assert jar.size == 3
    jar.withdraw(2)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(3)
