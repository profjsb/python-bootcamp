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

    def dothings(self, times):
        """ A method which takes a list
              of times (hours between 0 and 24) and
              returns a list of what the animal is 
              (randomly) doing.
         - Beyond hours 0 to 24: the animal does: ""
        """
        out_behaves = []
        for t in times:
            if (t < 0) or (t > 24):
                out_behaves.append('')
            elif ((self.name == 'owl') and
                (t > 6.0) and (t < 20.00)):
                out_behaves.append('sleep')
            else:
                out_behaves.append( \
                 self.animal_defs[self.name]['move'])
        return out_behaves


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


if __name__ == '__main__':
    ### The above line is Python syntax which defines a 
    ### section that is only used when animals_?.py is either:
    #   - executed from the shell as an executable script
    #   - executed from the shell using:  python animals_?.py
    #   - executed using another program, eg: python pdb.py animals_?.py
    #
    # This section is not used when nose_example1 is imported as a module.


    c = Animal('cat')
    o = Animal('owl')
    f = Animal('fish')

    times = []
    for i in xrange(10):
        times.append(random() * 24.)
    times.sort()
    
    c_do = c.dothings(times)
    o_do = o.dothings(times)
    f_do = f.dothings(times)

    for i in xrange(len(times)):
        print "time=%3.3f cat=%s owl=%s fish=%s" % ( \
                   times[i], c_do[i], o_do[i], f_do[i])
