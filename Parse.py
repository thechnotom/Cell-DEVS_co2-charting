from DataPoint import DataPoint

class Parse:

    # Consult the file for each cell query
    @staticmethod
    def getCellStates (filename, coords):
        dataPoints = []
        currTime = 0
        with open(filename, "r") as f:
            for line in f:
                # Update time
                if (Parse.isTime(line)):
                    # If there is no cell with the given coordinates in a particular time, use the previous
                    if (currTime > 0 and len(dataPoints) > 0 and dataPoints[-1].getTime() != currTime):
                        dataPoints.append(DataPoint(currTime, dataPoints[-1].getConcentration()))
                    currTime = int(line)
                    continue

                # Adds cell to list
                if (Parse.matchesCoords(line, coords)):
                    dataPoint = Parse.getDataPoint(currTime, line)
                    if (dataPoint not in dataPoints):
                        dataPoints.append(dataPoint)
        return dataPoints

    @staticmethod
    def getAllCellStates (filename):
        dataPoints = {}
        currTime = 0
        currCoords = ""
        with open(filename, "r") as f:
            for line in f:
                # Update time
                if (Parse.isTime(line)):
                    currTime = int(line)
                    continue

                currCoords = Parse.getCoordsString(Parse.getCoords(line))
                dataPoint = Parse.getDataPoint(currTime, line)
                if (currCoords not in dataPoints):
                    dataPoints[currCoords] = [dataPoint]
                elif (dataPoint not in dataPoints[currCoords]):
                    dataPoints[currCoords].append(dataPoint)

        print("Cleaning data points...")
        return Parse.cleanDataPoints(filename, dataPoints)

    @staticmethod
    def cleanDataPoints (filename, dataPoints):
        maxTime = Parse.getMaxTime(filename)
        for key in dataPoints:
            for i in range(0, maxTime):
                if (i < len(dataPoints[key])):
                    if (dataPoints[key][i].getTime() != i):
                        dataPoints[key].insert(i, DataPoint(i, dataPoints[key][i - 1].getConcentration()))
                else:
                    dataPoints[key].append(dataPoints[key][-1])
        return dataPoints

    @staticmethod
    def getMaxTime (filename):
        time = -1
        with open(filename, "r") as f:
            for line in f:
                if (Parse.isTime(line)):
                    time = int(line)
        return time

    @staticmethod
    def matchesCoords (line, coords):
        return coords == Parse.getCoords(line)

    @staticmethod
    def getCoords (line):
        return [int(element) for element in line[line.find("(") + 1:line.find(")")].split(",")]

    @staticmethod
    def getCoordsString (coords):
        result = ""
        for coord in enumerate(coords):
            result += str(coord[1])
            if (coord[0] != len(coords) - 1):
                result += ","
        return result

    @staticmethod
    def getDataPoint (time, line):
        return DataPoint(time, [int(element) for element in line[line.rfind("<") + 1:line.rfind(">")].split(",")][1])

    @staticmethod
    def isTime (line):
        try:
            int(line)
            return True
        except:
            return False