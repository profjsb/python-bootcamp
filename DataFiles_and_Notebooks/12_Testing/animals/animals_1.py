""" 
Test Driven Development using animals and Nose testing.
"""
class Animal:
    """ This is an animal.
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
