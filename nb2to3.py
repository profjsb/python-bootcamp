#!/usr/bin/env python3
"""
To run: python3 nb2to3.py notebook-or-directory
"""
# Authors: Thomas Kluyver, Fernando Perez
# See: https://gist.github.com/takluyver/c8839593c615bb2f6e80

import argparse
import pathlib
from nbformat import read, write

import lib2to3
from lib2to3.refactor import RefactoringTool, get_fixers_from_package


def refactor_notebook_inplace(rt, path):
    
    def refactor_cell(src):
        #print('\n***SRC***\n', src)
        try:
            tree = rt.refactor_string(src+'\n', str(path) + '/cell-%d' % i)
        except (lib2to3.pgen2.parse.ParseError,
                lib2to3.pgen2.tokenize.TokenError):
            return src
        else:
            return str(tree)[:-1]

    
    print("Refactoring:", path)
    nb = read(str(path), as_version=4)
    
    # Run 2to3 on code
    for i, cell in enumerate(nb.cells, start=1):
        if cell.cell_type == 'code':
            if cell.execution_count in ('&nbsp;', '*'):
                cell.execution_count = None

            if cell.source.startswith('%%'):
                # For cell magics, try to refactor the body, in case it's
                # valid python
                head, source = cell.source.split('\n', 1)
                cell.source = head + '\n' + refactor_cell(source)
            else:
                cell.source = refactor_cell(cell.source)
                   

    # Update notebook metadata
    nb.metadata.kernelspec = {
        'display_name': 'Python 3',
        'name': 'python3',
        'language': 'python',
    }
    if 'language_info' in nb.metadata:
        nb.metadata.language_info.codemirror_mode = {
            'name': 'ipython',
            'version': 3,
        }
        nb.metadata.language_info.pygments_lexer = 'ipython3'
        nb.metadata.language_info.pop('version', None)

    write(nb, str(path))

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('path', type=pathlib.Path,
        help="Notebook or directory containing notebooks")
    
    options = ap.parse_args(argv)
    
    avail_fixes = set(get_fixers_from_package('lib2to3.fixes'))
    rt = RefactoringTool(avail_fixes)
    
    if options.path.is_dir():
        for nb_path in options.path.rglob('*.ipynb'):
            refactor_notebook_inplace(rt, nb_path)
    else:
        refactor_notebook_inplace(rt, options.path)

if __name__ == '__main__':
    main()
