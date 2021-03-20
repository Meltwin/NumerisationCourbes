import tkinter as tk
import GUI.config.render as conf


class RenderFrame(tk.Frame):
    """
    Create a rendering frame to view the image after changing filter properties and add possibility of interaction
    """
    def __init__(self, parent):
        super(RenderFrame, self).__init__(parent)

        self.__canvas = RenderCanvas(self)
        self.__canvas = RenderMask(self)

        self.pack(fill=tk.BOTH, expand=1)


class RenderCanvas(tk.Canvas):
    """
    Canvas to show the rendered image
    """
    def __init__(self, parent: RenderFrame):
        super(RenderCanvas, self).__init__(parent, width=conf.RENDER_WIDTH, height=conf.RENDER_HEIGHT)
        self.create_rectangle(0, 0, conf.RENDER_WIDTH, conf.RENDER_HEIGHT, fill="#000000")

        self.place(x=0, y=0)


class RenderMask(tk.Canvas):
    """
    Canvas to show the rendered image
    """
    def __init__(self, parent: RenderFrame):
        super().__init__(parent, width=200, height=200)
        self.create_rectangle(0, 0, 200, 200, fill="#FF0000")

        self.place(x=0, y=0)
