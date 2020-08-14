# https://docs.python.org/3/library/tkinter.html

from Actions import Actions
import tkinter.filedialog
import tkinter as tk

class Interface (tk.Frame):

    def __init__ (self, master=None, filename="", transient=True):
        super().__init__(master)
        self.graphThread = None  # used when generating graphs
        self.loadThread = None  # used when loading in cell data (non-transient mode only)
        self.filename = filename
        self.transient = transient
        self.cellDict = {}
        self.master = master
        self.master.title("Graph Generator")
        self.pack()
        self.createWidgets()
        if (filename != ""):
            self.createCellDictionary()

    def createWidgets (self):
        # Coordinate information
        self.labelFrame_coords = tk.LabelFrame(self, text="Coordinates and Graphing")
        self.labelFrame_coords.pack(side="top", padx=5, pady=5)

        self.stringVar_entry_coords = tk.StringVar()
        self.entry_coords = tk.Entry(self.labelFrame_coords, textvariable=self.stringVar_entry_coords)
        self.entry_coords.insert(0, "ex. \"12,15\"")
        self.entry_coords.pack(side="left", padx=5, pady=5)

        self.button_generateGraph = tk.Button(self.labelFrame_coords)
        self.button_generateGraph["text"] = "Generate Graph"
        self.button_generateGraph["command"] = self.buttonCB_generateGraph
        self.button_generateGraph.pack(side="right", padx=5, pady=5)

        # File information
        self.labelFrame_file = tk.LabelFrame(self, text="File Information")
        self.labelFrame_file.pack(padx=5, pady=5)

        self.button_fileSelect = tk.Button(self.labelFrame_file)
        self.button_fileSelect["text"] = "Select File"
        self.button_fileSelect["command"] = self.buttonCB_fileSelect
        self.button_fileSelect.pack(side="left", padx=5, pady=5)

        self.stringVar_filename = tk.StringVar()
        Interface.setFilenameStringVar(self.stringVar_filename, self.filename)
        self.label_filename = tk.Label(self.labelFrame_file, textvariable=self.stringVar_filename)
        self.label_filename.pack(side="right", padx=5, pady=5)

        # Status information
        self.labelFrame_status = tk.LabelFrame(self, text="Status")
        self.labelFrame_status.pack(side="bottom", padx=5, pady=5)

        self.stringVar_status = tk.StringVar()
        if (self.filename != ""):
            self.stringVar_status.set("Enter coordinates")
        else:
            self.stringVar_status.set("Select file and enter coordinates")
        self.label_status = tk.Label(self.labelFrame_status, textvariable=self.stringVar_status)
        self.label_status.pack(side="right", padx=5, pady=5)

    def buttonCB_generateGraph (self):
        if (not self.transient and len(self.cellDict) == 0):
            self.stringVar_status.set("No cells have been loaded")
            return

        try:
            coords = [int(x.strip()) for x in self.stringVar_entry_coords.get().split(",")]
        except ValueError:
            self.stringVar_status.set("Invalid coordinate format")
            print(f"WARNING: Invalid coordinate string ({self.stringVar_entry_coords.get()})")
            return
        self.stringVar_status.set("Searching for coordinates...")
        self.update()

        # Make the variable accessible from within the thread
        graphicalElements = {
            "statusLabel" : self.stringVar_status,
            "graphButton" : self.button_generateGraph
        }
        if (self.transient):
            #result = Actions.generateGraph(filename=self.filename, coords=coords)
            self.graphThread = Actions.GraphThread(graphicalElements=graphicalElements, filename=self.filename, coords=coords)
        else:
            #result = Actions.generateGraph(cellDict=self.cellDict, coords=coords)
            self.graphThread = Actions.GraphThread(graphicalElements=graphicalElements, cellDict=self.cellDict, coords=coords)

        # Do not wait for this thread (it disables the graph generation button until completed)
        # The thread is a daemon and will terminate when finished or when the main thread terminates
        self.graphThread.start()

    def buttonCB_fileSelect (self):
        if (self.loadThread is not None and self.loadThread.isAlive()):
            self.stringVar_status.set("Populating data point storage...")
            return
        filename = tk.filedialog.askopenfilename(initialdir=".", title="Select File")
        if (filename != ""):
            self.filename = filename
            Interface.setFilenameStringVar(self.stringVar_filename, self.filename)
            self.createCellDictionary()

    def createCellDictionary (self):
        if (not self.transient):
            self.stringVar_status.set("Populating data point storage...")
            self.update()
            print("Populating data point storage...")

            # Make the variable accessible from within the thread
            graphicalElements = {
                "statusLabel" : self.stringVar_status,
                "graphButton" : self.button_generateGraph,
                "fileButton" : self.button_fileSelect
            }

            self.loadThread = Actions.LoadThread(graphicalElements=graphicalElements, filename=self.filename, cellDict=self.cellDict)

            # Do not wait for this thread (it disables the graph generation button until completed)
            # The thread is a daemon and will terminate when finished or when the main thread terminates
            self.loadThread.start()

    @staticmethod
    def setFilenameStringVar (stringVar, string):
        stringStart = ""
        if (len(string) > 25):
            stringStart = "..."
        stringVar.set(stringStart + string[-25:])

    @staticmethod
    def start (filename="", transient=True):
        root = tk.Tk()
        app = Interface(master=root, filename=filename, transient=transient)
        app.mainloop()