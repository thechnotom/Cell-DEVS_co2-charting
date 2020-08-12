from DataPoint import DataPoint

class Parse:

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
                    dataPoints.append(Parse.getDataPoint(currTime, line))
        return dataPoints

    @staticmethod
    def matchesCoords (line, coords):
        return coords == [int(element) for element in line[line.find("(") + 1:line.find(")")].split(",")]

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