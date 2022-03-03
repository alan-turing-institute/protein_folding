"""
Heavily based on
https://github.com/haddocking/pdb-tools/blob/master/pdbtools/pdb_merge.py
"""

import os
import sys

def check_input(args):

    if len(args) != 2:
        raise ValueError("Exactly two input files required")

    """Checks whether to read from stdin/file and validates user input/options.
    """

    # Defaults
    fl = []  # file list

    if len(args) >= 1:
        for fn in args:
            if not os.path.isfile(fn):
                emsg = 'ERROR!! File not found or not readable: \'{}\'\n'
                sys.stderr.write(emsg.format(fn))
                sys.stderr.write(__doc__)
                sys.exit(1)

            fh = open(fn, 'r')
            fl.append(fh)

    else:  # Whatever ...
        sys.stderr.write(__doc__)
        sys.exit(1)

    return fl

def run(chem_file, geom_file):
    """
    Iterate over both files. Takes chemistry from `chem_file` and geometry from `geom_file`.
    yields each line sequentially.
    Parameters
    ----------
    chem_file, geom_file : file-like objects
        Must handle `.close()` attribute.
    Yields
    ------
    str (line-by-line)
        Lines from the merged PDB files.
    """

    for chem_line, geom_line in zip(chem_file, geom_file):

        new_line = "{}{}{}".format(
            chem_line[:32],
            geom_line[32:56],
            chem_line[56:]
        )

        yield new_line

    chem_file.close()
    geom_file.close()



def main():
    # Check Input
    chem_file, geom_file = check_input(sys.argv[1:])

    # Do the job
    new_pdb = run(chem_file, geom_file)

    try:
        _buffer = []
        _buffer_size = 5000  # write N lines at a time
        for lineno, line in enumerate(new_pdb):
            if not (lineno % _buffer_size):
                sys.stdout.write(''.join(_buffer))
                _buffer = []
            _buffer.append(line)

        sys.stdout.write(''.join(_buffer))
        sys.stdout.flush()
    except IOError:
        # This is here to catch Broken Pipes
        # for example to use 'head' or 'tail' without
        # the error message showing up
        pass

    sys.exit(0)


if __name__ == '__main__':
    main()







