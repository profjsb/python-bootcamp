""" 
Test Driven Development using animals and Nose testing.
"""
from random import random

class Animal:
    """ This is an animal
    """
    animal_defs = {'owl':{'move':'fly',
                          'speak':'hoot'},
                   'cat':{'move':'walk',
                          'speak':'meow'},
                   'fish':{'move':'swim',
                          'speak':''}}
    def __init__(self, name):
        self.name = name

    def move(self):
        return self.animal_defs[self.name]['move']
        
    def speak(self):
        return self.animal_defs[self.name]['speak']


def test_moves():
    assert Animal('owl').move() == 'fly'
    assert Animal('cat').move() == 'walk'
    assert Animal('fish').move() == 'swim'

def test_speaks():
    assert Animal('owl').speak() == 'hoot'
    assert Animal('cat').speak() == 'meow'
    assert Animal('fish').speak() == ''

def test_dothings_list():
    """ Test that the animal does the same number of things as the number of hour-times given.
    """
    times = []
    for i in xrange(5):
        times.append(random() * 24.)
    for a in ['owl', 'cat', 'fish']:
        assert len(Animal(a).dothings(times)) ==\
                                         len(times)

def test_dothings_with_beyond_times():
    for a in ['owl', 'cat', 'fish']:
        assert Animal(a).dothings([-1]) == ['']
        assert Animal(a).dothings([25]) == ['']

def test_nocturnal_sleep():
    """ Test that an owl is awake at night.
    """
    night_hours = [0.1, 3.3, 23.9]
    noct_behaves = Animal('owl').dothings(night_hours)
    for behave in noct_behaves:
        assert behave != 'sleep'
