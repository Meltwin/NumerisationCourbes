from typing import Tuple
from Processing import Process
from numpy import ndarray, zeros


class Isolator(Process):
    """
    Return a 1bit image
        - pixel 0 : the color is too far
        - pixel 1 : the color is close enough
    """
    def __init__(self, color: Tuple[float, float, float], max_dist: float) -> None:
        """
        :param color: the wanted color
        :param max_dist: the maximum distance from the the color allowed (in [0,1])
        """
        super().__init__()

        # Tables
        self.__img_to_process: ndarray = None
        self.__distances = None

        # Properties
        self.__color_changed = True
        self.__color = color
        self.__dist = max_dist**2

    def set_color(self, color: Tuple[float, float, float]) -> None:
        """
        Change the selected color

        :param color: the wanted color
        """
        self.__color_changed = True
        self.__color = color

    def set_dist(self, dist: float) -> None:
        """
        Change the maximum distance allowed

        :param dist: the new distance in the rgb base
        """
        self.__dist = dist**2

    def run(self, img: ndarray) -> ndarray:
        # Check if the img is the same -> don't make new calculations
        # except if the color has change
        if self.__img_to_process is not img or self.__color_changed:
            print("[ Color ] Run distance calculations")
            self.__img_to_process = img
            self.__calc_distance__()
            print("[ Color ] Distances calculated")

        # Select the colors
        l, r, _ = img.shape
        self._img = zeros((l, r))
        for y in range(l):
            for x in range(r):
                if self.__distances[y, x] <= self.__dist:
                    self._img[y, x] = 1
        print("[ Color ] Isolation done", end="\n\n")
        return self._img

    # ------------------------------------------ #
    #              Distances section             #
    # ------------------------------------------ #
    def __calc_distance__(self) -> None:
        # Init distance table
        l, r, c = self.__img_to_process.shape
        self.__distances = zeros([l, r])

        # Read all the pixels
        for y in range(l):
            for x in range(r):
                self.__distances[y, x] = self.__distance(self.__img_to_process[y, x])
        self.__color_changed = False

    def __distance(self, color):
        return (self.__color[0]-color[0])**2 + (self.__color[1]-color[1])**2 + (self.__color[2]-color[2])**2
