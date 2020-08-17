# Carleton University (ARSLab)
# Thomas Roller

import plotly.express as px
import pandas as pd

# Class: Graph
# Purpose: provide graph-creation capabilities
# Arguments:
#     none
class Graph:

    # Function: createDataFrame
    # Purpose: create a representation of the data which can be used to generate graphs
    # Arguments:
    #     dataPoints: a list of DataPoints to be used
    # Return:
    #     a DataFrame object representing a list of DataPoints
    @staticmethod
    def createDataFrame (dataPoints):
        points = [x.toArray() for x in dataPoints]
        return pd.DataFrame(data=points, columns=["time", "concentration"])

    # Function: getRange
    # Purpose: get the minimum and maximum values for concentration to be used on a graph
    # Arguments:
    #     dataPoints: list of DataPoints to be checked
    # Return:
    #     minimum and maximum values for the graph's concentration axis
    @staticmethod
    def getRange (dataPoints):
        return [min(dataPoints).getConcentration() - 10, max(dataPoints).getConcentration() + 10]

    # Function: getTitle
    # Purpose: create a title for a graph
    # Arguments:
    #     coords: coordinates for which the graph will show concentration
    # Return:
    #     a string representing the title of the graph
    @staticmethod
    def getTitle (coords):
        title = "CO2 Concentration at Cell ("
        for coord in enumerate(coords):
            title += str(coord[1])
            if (coord[0] != len(coords) - 1):
                title += ", "
        return title + ") vs. Time"

    # Function: generateGraph
    # Purpose: create and show a graph
    # Arguments:
    #     dataPoints: dataPoints to be used to generate a graph
    #     coords: coordinates for which the graph will show concentration
    # Return:
    #     none
    @staticmethod
    def generateGraph (dataPoints, coords):
        dataFrame = Graph.createDataFrame(dataPoints)
        graph = px.bar(dataFrame, x="time", y="concentration", range_y=Graph.getRange(dataPoints), title=Graph.getTitle(coords))
        graph.show()