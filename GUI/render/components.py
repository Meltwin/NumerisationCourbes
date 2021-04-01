import tkinter as tk
from math import floor, ceil

import GUI.config.render as conf
from Lib.image import Image
from Lib.generator import un_parallel_grow


class RenderCanvas(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=conf.RENDER_WIDTH+300, height=conf.RENDER_HEIGHT, bg=str(conf.BACKGROUND_COLOR))
        self.__img = Image((0, 0))
        self.__rat = 1

        self.pack()

    def show_img(self, img: Image):
        self.__img = img
        self.__render()

    def __render(self) -> None:
        self.clear()
        self.__get_ratio()
        self.__calc_margin()
        self.__show()

    # Calculations
    def __get_ratio(self) -> None:
        """
        Calculate the ratio to scale the image for showing in the canvas
        """
        i_size = self.__img.get_size()

        rat_x = conf.RENDER_WIDTH/i_size[0]
        rat_y = conf.RENDER_HEIGHT/i_size[1]
        print(rat_x, rat_y)

        self.__rat = min(rat_x, rat_y)

    def __calc_margin(self):
        i_size = self.__img.get_size()

        new_x = i_size[0] * self.__rat
        new_y = i_size[1] * self.__rat

        # Margins
        dx = (conf.RENDER_WIDTH-new_x)/2
        self.__mx = (floor(dx), ceil(dx))

        dy = (conf.RENDER_HEIGHT-new_y)/2
        self.__my = (floor(dy), ceil(dy))

    # Show in the correct scale
    def __show(self):
        """
        If the image is too big, show it with less pixels
        :return:
        """
        for (nx, ix) in un_parallel_grow(self.__mx[0], conf.RENDER_WIDTH, self.__rat):
            for (ny, iy) in un_parallel_grow(self.__my[0], conf.RENDER_HEIGHT, self.__rat):
                self.create_line(nx, ny, nx+1, ny, fill=str(self.__img.get(ix, iy)))
        self.create_rectangle(0, 0, 501, self.__my[0], fill='#FF0000')
        self.create_rectangle(0, 500, 501, 500-self.__my[1], fill='#FF0000')

    def clear(self):
        self.create_rectangle(0, 0, conf.RENDER_WIDTH, conf.RENDER_HEIGHT, fill=str(conf.BACKGROUND_COLOR))
