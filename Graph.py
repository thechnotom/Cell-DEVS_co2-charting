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
    def generateGraph (dataPoints):
        dataFrame = Graph.createDataFrame(dataPoints)
        graph = px.bar(dataFrame, x="time", y="concentration", range_y=Graph.getRange(dataPoints))
        graph.show()