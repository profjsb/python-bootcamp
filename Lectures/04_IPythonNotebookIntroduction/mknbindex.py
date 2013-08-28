#!/usr/bin/env python
"""Simple script to auto-generate the index of notebooks in a given directory.
"""

import glob
import urllib

notebooks = sorted(glob.glob('*.ipynb'))

tpl = ( '* [{0}](http://nbviewer.ipython.org/url/raw.github.com/profjsb/python-bootcamp/master/Lectures/04_IPythonNotebookIntroduction/{1})' )


idx = [
"""Introduction to IPython
=======================

These notebooks introduce the basics of IPython, as part of the [Berkeley Python
Bootcamp](http://pythonbootcamp.info).

"""]

idx.extend(tpl.format(nb.replace('.ipynb',''), urllib.quote(nb))
           for nb in notebooks)

with open('README.md', 'w') as f:
    f.write('\n'.join(idx))
    f.write('\n')
