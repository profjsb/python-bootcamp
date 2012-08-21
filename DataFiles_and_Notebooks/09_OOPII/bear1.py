class Bear:
    """
    class to show off addition (and multiplication)
    """
    bear_num = 0
    def __init__(self,name):
        self.name = name
        print " made a bear called %s" % (name)
        Bear.bear_num += 1
        self.my_num = Bear.bear_num

    def __add__(self,other):
        ## spawn a little tike
        cub = Bear("progeny_of_%s_and_%s" % (self.name,other.name))
        cub.parents = (self,other)
        return cub

    def __mul__(self,other):
        ## multiply (as in "go forth and multiply") is really the same as adding
        self.__add__(other)
        