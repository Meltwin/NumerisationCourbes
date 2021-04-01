from Lib.colors import BaseColor, RGBColor, Color
from Lib.generator import rectangular
from typing import Tuple
import numpy as np


class Image:
    def __init__(self, size: Tuple[int, int] = (0, 0)):
        """
        Create an Image instance with the given size
        """
        self._size = size
        self._make_array()

    def set_size(self, columns: int, row: int):
        self._size = (columns, row)
        self._make_array()

    def get_size(self): return self._size

    def _make_array(self):
        self._table = [[BaseColor() for i in range(self._size[1])] for j in range(self._size[0])]

    def fill(self, img: np.ndarray) -> None:
        m, n, c = img.shape
        self.set_size(n, m)
        for (x, y) in rectangular(0, 0, n, m):
            self._table[x][y] = RGBColor(Color.red2int(img[y, x][0]),
                                         Color.red2int(img[y, x][1]),
                                         Color.red2int(img[y, x][2]))

    def set(self, column: int, row: int, color: BaseColor) -> None:
        self._table[column][row] = color

    def get(self, column: int, row: int) -> BaseColor: return self._table[column][row]

    def __str__(self):
        return str(self._table)
