class Plant:
    num_known = 0
    def __init__(self,common_name,latin_name=None):
        self.latin_name = latin_name
        self.common_name = common_name
        Plant.num_known += 1
    
    def __str__(self):
        return "I am a plant (%s)!" % self.common_name

class Flower(Plant):
    has_pedals = True

    def __init__(self,common_name,npedals=5,pedal_color="red",latin_name=None):
        ## call the __init__ of the 
        Plant.__init__(self,common_name,latin_name=latin_name)
        self.npedals=5
        self.pedal_color = pedal_color
        
    def __str__(self):
        return "I am a flower (%s)!" % self.common_name
            


class A:
    def __init__(self):
        print "A"
class B(A):
    def __init__(self):
        A.__init__(self)
        print "B"