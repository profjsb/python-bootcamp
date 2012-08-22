""" Nose Example 1
"""

class Transmogrifier:
    """ An important class
    """
    def transmogrify(self, person):
        """ Transmogrify someone
        """
        transmog = {'calvin':'tiger',
                     'hobbes':'chicken'}
        new_person = transmog[person]
        return new_person


def test_transmogrify():
    TM = Transmogrifier()
    for p in ['Calvin', 'Hobbes']:
        assert TM.transmogrify(p) != None


def main():
    TM = Transmogrifier()
    for p in ['calvin', 'Hobbes']:
        print p, '->  ZAP!  ->', TM.transmogrify(p)


if __name__ == '__main__':
    ### The above line is Python syntax which defines a 
    ### section that is only used when nose_example1.py is either:
    #   - executed from the shell as an executable script
    #   - executed from the shell using:  python nose_example1.py
    #   - executed using another program, eg: python pdb.py nose_example1.py
    #
    # This section is not used when nose_example1 is imported as a module.

    main()

