from Parse import Parse
from Graph import Graph
import time

class Actions:

    @staticmethod
    def generateGraph (filename, coords):
        print(f"Parsing file ({filename}) for coords: {coords}")

        startTime = time.monotonic()
        dataPoints = Parse.getCellStates(filename, coords)
        endTime = time.monotonic()

        print(f"Parse complete")

        print(f"Time taken: {endTime - startTime}s")
        print(f"Number of cells: {len(dataPoints)}")

        if (len(dataPoints) == 0):
            print("No data points found (cannot generate graph)")
            return

        Graph.generateGraph(dataPoints, coords)