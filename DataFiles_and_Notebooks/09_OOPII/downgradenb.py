"""Simple utility script for semi-gracefully downgrading v3 notebooks to v2"""

import io
import os
import sys

from IPython.nbformat import current

def heading_to_md(cell):
    """turn heading cell into corresponding markdown"""
    cell.cell_type = "markdown"
    level = cell.pop('level', 1)
    cell.source = '#'*level + ' ' + cell.source

def raw_to_md(cell):
    """let raw passthrough as markdown"""
    cell.cell_type = "markdown"

def downgrade(nb):
    """downgrade a v3 notebook to v2"""
    if nb.nbformat != 3:
        return nb
    nb.nbformat = 2
    for ws in nb.worksheets:
        for cell in ws.cells:
            if cell.cell_type == 'heading':
                heading_to_md(cell)
            elif cell.cell_type == 'raw':
                raw_to_md(cell)
    return nb

def downgrade_ipynb(fname):
    base, ext = os.path.splitext(fname)
    newname = base+'.v2'+ext
    print "downgrading %s -> %s" % (fname, newname)
    with io.open(fname, 'r', encoding='utf8') as f:
        nb = current.read(f, 'json')
    nb = downgrade(nb)
    with open(newname, 'w') as f:
        current.write(nb, f, 'json')

if __name__ == '__main__':
    map(downgrade_ipynb, sys.argv[1:])
