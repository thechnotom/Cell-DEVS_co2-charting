class DataPoint:

    def __init__ (self, time, conc):
        self.time = time
        self.conc = conc

    def getTime (self):
        return self.time

    def getConcentration (self):
        return self.conc

    def copy (self):
        return DataPoint(self.time, self.conc)

    def __str__ (self):
        return f"{self.time}:{self.conc}"