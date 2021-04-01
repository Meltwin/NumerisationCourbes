import tkinter as tk
import numpy as np
from typing import Tuple

import GUI.render.components as comp
from Processing import ImageLoader


class RenderFrame(tk.Frame):
    """
    Create a rendering frame to view the image after changing filter properties and add possibility of interaction
    """
    def __init__(self, parent):
        super(RenderFrame, self).__init__(parent, bg="#598099")

        self.__canvas = comp.RenderCanvas(self)

        img = ImageLoader("./imgs/c0_redu.png")
        img.run()

        self.__canvas.show_img(img.get_img())

        self.pack(fill=tk.BOTH, expand=1)

    def show_img(self, img: np.ndarray) -> None:
        pass

    def show_points(self, points: Tuple[int, int]) -> None:
        pass
