from twttr import shorten
import pytest

def test_lowercase():
    assert shorten('hi guys') == 'h gys'
    assert shorten('kwasi') == 'kws'
    assert shorten('ama') == 'm'

def test_uppercase():
    assert shorten('HALLO') == 'HLL'
    assert shorten('INSTA') == 'NST'
    assert shorten('PAPAER') == 'PPR'

def test_input():
    assert shorten('1234') == '1234'

def test_punc():
    assert shorten('hi!') == 'h!'
    assert shorten("isn't he here yet") == "sn't h hr yt"
