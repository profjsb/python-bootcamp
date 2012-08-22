""" 
Test Driven Development using animals and Nose testing.
"""

def test_moves():
    assert Animal('owl').move() == 'fly'
    assert Animal('cat').move() == 'walk'
    assert Animal('fish').move() == 'swim'

def test_speaks():
    assert Animal('owl').speak() == 'hoot'
    assert Animal('cat').speak() == 'meow'
    assert Animal('fish').speak() == ''
