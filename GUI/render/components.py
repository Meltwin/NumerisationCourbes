import tkinter as tk
import GUI.config.render as conf


class BaseRenderCanvas(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=conf.RENDER_WIDTH, height=conf.RENDER_HEIGHT)
