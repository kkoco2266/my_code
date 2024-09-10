from working import convert
import pytest

def test_input():
    assert convert('3 AM to 5 PM') == '03:00 to 17:00'
    assert convert('3 PM to 5 AM') == '15:00 to 05:00'
    with pytest.raises(ValueError):
        convert('3AM to 5 PM')
    with pytest.raises(ValueError):
        convert('3 AM to 5PM')
    with pytest.raises(ValueError):
        convert('3:60 AM to 5 PM')

def test_withmins():
    assert convert('3:09 PM to 4:10 PM') == '15:09 to 16:10'
    assert convert('10:19 PM to 4:10 PM') == '22:19 to 16:10'
    assert convert('3:09 PM to 12:17 PM') == '15:09 to 12:17'
    assert convert('12:49 AM to 4:10 PM') == '00:49 to 16:10'

def test_nomins():
    assert convert('3 PM to 5 PM') == '15:00 to 17:00'
    assert convert('3 AM to 5 AM') == '03:00 to 05:00'
    assert convert('12 AM to 5 PM') == '00:00 to 17:00'
    assert convert('3 AM to 12 PM') == '03:00 to 12:00'

def test_omit():
    with pytest.raises(ValueError):
        convert('3 PM - 3 AM')
def test_omit0():
    with pytest.raises(ValueError):
        convert('11 PM - 3 AM')
def test_omit1():
    with pytest.raises(ValueError):
        convert('12 PM - 8 AM')
def test_omit2():
    with pytest.raises(ValueError):
        convert('10 PM - 4 AM')

def test_omi():
    with pytest.raises(ValueError):
        convert('15 PM to 3 AM')
    with pytest.raises(ValueError):
        convert('11 PM to 13 AM')
    with pytest.raises(ValueError):
        convert('10 PM to 30 AM')
    with pytest.raises(ValueError):
        convert('19 PM to 3 AM')
