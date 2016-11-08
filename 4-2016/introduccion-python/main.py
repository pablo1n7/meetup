#!/usr/bin/env python3
"""Module docstring.

This serves as a long usage message.
"""
import sys
import getopt
from paquete.fibo import *

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(argv[1:], "hf:v", ["help", "fibo"])
    except getopt.error as msg:
        print(msg, file=sys.stderr)
        print("for help use --help", file=sys.stderr)
        return 2
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print(__doc__)
            return 0
        elif o in ("-f", "--fibo"):
            print(fib2(int(a)))
            return 0
    # process arguments
    for arg in args:
        print(arg)

if __name__ == "__main__":
    sys.exit(main())