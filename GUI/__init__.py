import tkinter as tk
import GUI.projectList as pl
import GUI.render as render
from GUI.config.window import *


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title(WINDOW_NAME)
        self.minsize(WINDOW_DIM[0], WINDOW_DIM[1])
        self.config(background=WINDOW_BACKGROUND)

        self.process_list = pl.ProcessList(self)
        self.rendering = render.RenderFrame(self)

        self.mainloop()
