"demo file"

def foo():
    "This is a function"
    s = 'some string'
    a = 42
    b = bar()
    return a + b

def bar():
    """
    This function has a bug in it
    """
    a = 0
    return 1. / a # bug here!

