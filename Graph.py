import plotly.express as px
import pandas as pd

class Graph:

    @staticmethod
    def createDataFrame (dataPoints):
        points = [x.toArray() for x in dataPoints]
        return pd.DataFrame(data=points, columns=["time", "concentration"])

    @staticmethod
    def getRange (dataPoints):
        return [min(dataPoints).getConcentration() - 10, max(dataPoints).getConcentration() + 10]

    @staticmethod
    def getTitle (coords):
        title = "CO2 Concentration at Cell ("
        for coord in enumerate(coords):
            title += str(coord[1])
            if (coord[0] != len(coords) - 1):
                title += ", "
        return title + ") vs. Time"

    @staticmethod
    def generateGraph (dataPoints, coords):
        dataFrame = Graph.createDataFrame(dataPoints)
        graph = px.bar(dataFrame, x="time", y="concentration", range_y=Graph.getRange(dataPoints), title=Graph.getTitle(coords))
        graph.show()