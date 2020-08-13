from Parse import Parse
from Graph import Graph
import time

class Actions:

    @staticmethod
    def generateGraph (filename="", coords=None, cellDict=None):
        if (filename == "" and coords is not None and cellDict is not None):
            return Actions.generateGraph_query(cellDict, coords)
        elif (filename != "" and coords is not None and cellDict is None):
            return Actions.generateGraph_transient(filename, coords)
        else:
            print("WARNING: Invalid parameters")
            return False

    @staticmethod
    def generateGraph_transient (filename, coords):
        print(f"Parsing file ({filename}) for coords: {coords}")

        startTime = time.monotonic()
        dataPoints = Parse.getCellStates(filename, coords)
        endTime = time.monotonic()

        print(f"Parse complete")

        print(f"Time taken: {endTime - startTime}s")
        print(f"Number of cells: {len(dataPoints)}")

        if (len(dataPoints) == 0):
            print("No data points found (cannot generate graph)")
            return False

        Graph.generateGraph(dataPoints, coords)
        return True

    @staticmethod
    def generateGraph_query (cellDict, coords):
        print(f"Querying dictionary for coords: {coords}")

        coordsString = Parse.getCoordsString(coords)
        if (coordsString not in cellDict):
            return False

        dataPoints = cellDict[coordsString]

        print(f"Number of cells: {len(dataPoints)}")

        if (len(dataPoints) == 0):
            print("No data points found (cannot generate graph)")
            return False

        Graph.generateGraph(dataPoints, coords)
        return True

    @staticmethod
    def getAllCellStates (filename):
        print(f"Parsing file ({filename})")
        startTime = time.monotonic()
        states = Parse.getAllCellStates(filename)
        endTime = time.monotonic()
        print(f"Time taken: {endTime - startTime}s")
        return states