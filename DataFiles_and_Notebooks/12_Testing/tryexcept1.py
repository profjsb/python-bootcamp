import traceback
def example1():
    try:
        raise SyntaxError, "example"
    except:
        traceback.print_exc()
    print "...still running..."

def example2():
    """ Here we have access to the (filename, line number, function name, text)
    of each element in the Traceback stack.
    """
    try:
        raise SyntaxError
    except:
        stack_list = traceback.extract_stack()
        for (filename, linenum, functionname, text) in stack_list:
            print "%s:%d %s()" % (filename, linenum, functionname)
    print "...still running..."
