from Parse import Parse
from Graph import Graph
import time
import sys

filename = sys.argv[1]
coords = []
for i in range (2, len(sys.argv)):
    coords.append(int(sys.argv[i]))

# 2D test: [4, 42]
# 3D test: [25, 20, 3]

#filename = "data/output_messages.txt"
#filename = "data/state.txt"

print(f"Parsing: {filename}")

startTime = time.monotonic()
dataPoints = Parse.getCellStates(filename, coords)
endTime = time.monotonic()

print(f"Parse complete")

print(f"Time taken: {endTime - startTime}s")
print(f"Number of cells: {len(dataPoints)}")

if (len(dataPoints) == 0):
    print("No data points found (cannot generate graph)")
    sys.exit(1)

#for i in range(0, len(dataPoints)):
#    print(f"output {dataPoints[i]}")

Graph.generateGraph(dataPoints, coords)