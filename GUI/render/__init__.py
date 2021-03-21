import tkinter as tk
import numpy as np
from typing import Tuple

import GUI.config.render as conf
import GUI.render.components as comp
from Lib.color import RGBAColor


class RenderFrame(tk.Frame):
    """
    Create a rendering frame to view the image after changing filter properties and add possibility of interaction
    """
    def __init__(self, parent):
        super(RenderFrame, self).__init__(parent)

        self.__canvas = RenderCanvas(self)

        self.pack(fill=tk.BOTH, expand=1)

    def show_img(self, img: np.ndarray) -> None:
        pass

    def show_points(self, points: Tuple[int, int]) -> None:
        pass


class RenderCanvas(comp.BaseRenderCanvas):
    """
    Canvas to show the rendered image
    """
    def __init__(self, parent: RenderFrame):
        super(RenderCanvas, self).__init__(parent)
        c = RGBAColor(25, 17, 125, 1., 8)
        r = RGBAColor(100, 100, 100, .5, 8)
        c = c+r
        self.create_rectangle(0, 0, conf.RENDER_WIDTH, conf.RENDER_HEIGHT, fill=c.get_hex())

        self.place(x=0, y=0)


class RenderMask(comp.BaseRenderCanvas):
    """
    Canvas to show the rendered image
    """
    def __init__(self, parent: RenderFrame):
        super().__init__(parent)
        self.config(bg="transparent")
        self.create_rectangle(0, 0, 200, 200, fill="#FF0000")

        self.place(x=0, y=0)
