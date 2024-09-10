from fuel import convert, gauge
import pytest

def test_convert_0():
    assert convert('3/5') == 60
    assert convert('1/100') == 1

def test_convert_1():
    with pytest.raises(ValueError):
        convert('4/3')

def test_convert_2():
    with pytest.raises(ZeroDivisionError):
        convert('4/0')

def test_guage_0():
    assert gauge(5) == '5%'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
