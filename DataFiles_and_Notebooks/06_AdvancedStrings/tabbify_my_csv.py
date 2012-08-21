"""
small copy program that turns a csv file into a tabbed file

  PYTHON BOOT CAMP EXAMPLE; 
    created by Josh Bloom at UC Berkeley, 2010,2012 (ucbpythonclass+bootcamp@gmail.com)

"""

import os

def tabbify(infilename,outfilename,ignore_comments=True,comment_chars="#;/"):
    """
INPUT: infilename
OUTPUT: creates a file called outfilename
    """
    if not os.path.exists(infilename):
        return  # do nothing if the file isn't there
    f = open(infilename,"r")
    o = open(outfilename,"w")
    inlines = f.readlines() ; f.close()
    outlines = []
    for l in inlines:
        if ignore_comments and (l[0] in comment_chars):
            outlines.append(l)
        else:
            outlines.append(l.replace(",","\t"))
    o.writelines(outlines) ; o.close()

