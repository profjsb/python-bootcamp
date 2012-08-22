def do_string_stuff(val):
    assert type(val) == type("")
    print ">" + val + "< length:", len(val)
    
def do_string_stuff_better(val):
    val_type = type(val)
    assert val_type == type(""), "Given a %s" % (str(val_type))
    print ">" + val + "< length:", len(val)
    
