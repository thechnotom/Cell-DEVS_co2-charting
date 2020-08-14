from Parse import Parse
from Graph import Graph
import time
import threading

class Actions:

    class GraphThread(threading.Thread):
        def __init__ (self, graphicalElements, filename="", coords=None, cellDict=None):
            super().__init__(daemon=True)
            self.filename = filename
            self.coords = coords
            self.cellDict = cellDict
            self.graphicalElements = graphicalElements

        def run (self):
            print(f"GraphThread.run: size of cellDict: {len(self.cellDict)}")
            self.graphicalElements["graphButton"]["state"] = "disable"
            result = Actions.generateGraph(self.filename, self.coords, self.cellDict)
            if (result[0]):
                self.graphicalElements["statusLabel"].set(f"Showing graph (elapsed: {round(result[1], 2)}s)")
            else:
                self.graphicalElements["statusLabel"].set("No data point matching coordinates found")
            self.graphicalElements["graphButton"]["state"] = "normal"

    class LoadThread(threading.Thread):
        def __init__ (self, graphicalElements, filename="", cellDict=None):
            super().__init__(daemon=True)
            self.filename = filename
            self.graphicalElements = graphicalElements
            self.cellDict = cellDict

        def run (self):
            self.graphicalElements["fileButton"]["state"] = "disable"
            self.graphicalElements["graphButton"]["state"] = "disable"
            result = Actions.getAllCellStates (self.filename)
            self.cellDict.clear()
            for key in result[0]:
                self.cellDict[key] = result[0][key]
            self.graphicalElements["fileButton"]["state"] = "normal"
            self.graphicalElements["graphButton"]["state"] = "normal"

            self.graphicalElements["statusLabel"].set(f"Storage populated (elapsed: {round(result[1], 2)}s)")
            print("Storage populated")

    @staticmethod
    def generateGraph (filename="", coords=None, cellDict=None):
        if (filename == "" and coords is not None and cellDict is not None):
            return Actions.generateGraph_query(cellDict, coords)
        elif (filename != "" and coords is not None and cellDict is None):
            return Actions.generateGraph_transient(filename, coords)
        else:
            print("WARNING: Invalid parameters")
            return [False, 0]

    @staticmethod
    def generateGraph_transient (filename, coords):
        print(f"Parsing file ({filename}) for coords: {coords}")

        startTime = time.monotonic()
        dataPoints = Parse.getCellStates(filename, coords)
        endTime = time.monotonic()

        print(f"Parse complete")

        timeElapsed = endTime - startTime
        print(f"Time taken: {timeElapsed}s")
        print(f"Number of cells: {len(dataPoints)}")

        if (len(dataPoints) == 0):
            print("No data points found (cannot generate graph)")
            return [False, timeElapsed]

        Graph.generateGraph(dataPoints, coords)
        return [True, timeElapsed]

    @staticmethod
    def generateGraph_query (cellDict, coords):
        print(f"Querying dictionary for coords: {coords}")

        coordsString = Parse.getCoordsString(coords)
        if (coordsString not in cellDict):
            print(f"Could not find the provided coordinate in the cell dictionary (length of cellDict: {len(cellDict)})")
            return [False, 0]

        startTime = time.monotonic()
        dataPoints = cellDict[coordsString]
        endTime = time.monotonic()

        timeElapsed = endTime - startTime
        print(f"Time taken: {timeElapsed}s")
        print(f"Number of cells: {len(dataPoints)}")

        if (len(dataPoints) == 0):
            print("No data points found (cannot generate graph)")
            return [False, timeElapsed]

        Graph.generateGraph(dataPoints, coords)
        return [True, timeElapsed]

    @staticmethod
    def getAllCellStates (filename):
        print(f"Parsing file ({filename})...")
        startTime = time.monotonic()
        states = Parse.getAllCellStates(filename)
        endTime = time.monotonic()
        timeElapsed = endTime - startTime
        print(f"Time taken: {timeElapsed}s")
        return [states, timeElapsed]