from typing import Tuple
from enum import Enum, unique, auto
from numpy import ndarray, zeros

from Processing import Process, table_course_gene


@unique
class SelOption(Enum):
    INCLUDE = auto()
    EXCLUDE = auto()


class Selector(Process):
    def __init__(self) -> None:
        super().__init__()
        self.__include = []
        self.__exclude = []

    def add_selection(self, zone: Tuple[Tuple[int, int], Tuple[int, int]], mode: SelOption = SelOption.EXCLUDE) -> None:
        """
        Add an area to be selected or excluded
        Included area are exclusives, excluded area is only meaningful in included area

        :param zone: the selected zone ( (x_min, y_min), (x_max, y_max))
        :param mode: the mode (include or exclude)
        """
        if mode is SelOption.EXCLUDE:
            self.__exclude.append(zone)
        elif mode is SelOption.INCLUDE:
            self.__include.append(zone)

    def run(self, img: ndarray):
        m, n = img.shape
        self._img = zeros((m, n))

        # Include zone
        print("[Select ] Including")
        for area in self.__include:
            for (x, y) in table_course_gene(min(area[1][1], n), min(area[1][0], m), area[0][1], area[0][0]):
                self._img[x][y] = img[x][y]

        # Excluded zone
        print("[Select ] Excluding")
        for area in self.__exclude:
            for (x, y) in table_course_gene(min(area[1][1], n), min(area[1][0], m), area[0][1], area[0][0]):
                self._img[x][y] = 0

        print("[Select ] Section done.", end="\n\n")
        return self._img
