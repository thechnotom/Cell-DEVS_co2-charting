from Interface import Interface
import sys

transient = True

if (len(sys.argv) > 1):
    Interface.start(filename=sys.argv[1], transient=transient)
else:
    Interface.start(transient=transient)