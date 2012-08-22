def divide_it(x, y):
    try:
        out = x / y
    except:
        print '   Divide by zero!'
        out = None
    return out
