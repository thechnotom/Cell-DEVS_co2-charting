from DataPoint import DataPoint

class Parse:

    @staticmethod
    def getCellStates (filename, coords):
        dataPoints = []
        currTime = 0
        not_added_counter = 0
        not_consecutive_times = 0
        equal_times = 0
        with open(filename, "r") as f:
            for line in f:
                # Update time
                if (Parse.isTime(line)):
                    if (currTime > 0 and dataPoints[-1].getTime() != currTime):
                        dataPoints.append(dataPoints[-1].copy())
                        not_added_counter += 1
                    if (currTime + 1 != int(line)):
                        not_consecutive_times += 1
                    if (currTime == int(line)):
                        equal_times += 1
                    currTime = int(line)
                    continue

                # Adds cell to list
                if (Parse.matchesCoords(line, coords)):
                    dataPoints.append(Parse.getDataPoint(currTime, line))
        print(f"Not added counter: {not_added_counter}")
        print(f"Not consecutive counter: {not_consecutive_times}")
        print(f"Equal times: {equal_times}")
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