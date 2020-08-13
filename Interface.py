# https://docs.python.org/3/library/tkinter.html

from Actions import Actions
import tkinter.filedialog
import tkinter as tk

class Interface (tk.Frame):

    def __init__ (self, master=None, filename=""):
        super().__init__(master)
        self.filename = filename
        self.master = master
        self.master.title("Graph Generator")
        self.pack()
        self.createWidgets()

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
        try:
            coords = [int(x.strip()) for x in self.stringVar_entry_coords.get().split(",")]
        except ValueError:
            self.stringVar_status.set("Invalid coordinate format")
            print(f"WARNING: Invalid coordinate string ({self.stringVar_entry_coords.get()})")
            return
        self.stringVar_status.set("Parsing file...")
        self.update()
        if (Actions.generateGraph(self.filename, coords)):
            self.stringVar_status.set("Parsing complete")
            return
        else:
            self.stringVar_status.set("No data point matching coordinates found")

    def buttonCB_fileSelect (self):
        filename = tk.filedialog.askopenfilename(initialdir=".", title="Select File")
        if (filename != ""):
            self.filename = filename
            Interface.setFilenameStringVar(self.stringVar_filename, self.filename)

    @staticmethod
    def setFilenameStringVar (stringVar, string):
        stringStart = ""
        if (len(string) > 25):
            stringStart = "..."
        stringVar.set(stringStart + string[-25:])

    @staticmethod
    def start (filename=""):
        root = tk.Tk()
        app = Interface(master=root, filename=filename)
        app.mainloop()