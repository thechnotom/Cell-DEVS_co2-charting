# https://docs.python.org/3/library/tkinter.html

from Actions import Actions
import tkinter as tk

class Interface (tk.Frame):

    def __init__ (self, master=None, filename=None):
        super().__init__(master)
        self.filename = filename
        self.master = master
        self.master.title("Graph Generator")
        self.pack()
        self.createWidgets()

    def createWidgets (self):
        self.stringVar_entry_coords = tk.StringVar()
        self.entry_coords = tk.Entry(self, textvariable=self.stringVar_entry_coords)
        self.entry_coords.insert(0, "ex. \"12,15,3\"")
        self.entry_coords.pack(side="left", padx=5, pady=5)

        self.button_generateGraph = tk.Button(self)
        self.button_generateGraph["text"] = "Generate Graph"
        self.button_generateGraph["command"] = self.buttonCB_generateGraph
        self.button_generateGraph.pack(side="right", padx=5, pady=5)

    def buttonCB_generateGraph (self):
        try:
            coords = [int(x.strip()) for x in self.stringVar_entry_coords.get().split(",")]
        except ValueError:
            print(f"WARNING: Invalid coordinate string ({self.stringVar_entry_coords.get()})")
            return
        Actions.generateGraph(self.filename, coords)

    @staticmethod
    def start (filename):
        root = tk.Tk()
        app = Interface(master=root, filename=filename)
        app.mainloop()