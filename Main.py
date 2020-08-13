from Interface import Interface
import sys

transient = False

if (len(sys.argv) > 1):
    Interface.start(filename=sys.argv[1], transient=transient)
else:
    Interface.start(transient=transient)