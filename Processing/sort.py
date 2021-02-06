from typing import List, Tuple

from enum import Enum, unique, auto

from Processing.process import PointProcess


@unique
class SortOrder(Enum):
    NORMAL = auto()
    CYCLE = auto()


# ===========================================================
#                      Sorting Algorithm
# ===========================================================
def _sort_asc(ref: Tuple[int, int], ptn: Tuple[int, int]) -> bool:
    return ref[1] < ptn[1] if ref[0] == ptn[0] else ref[0] > ptn[0]


def _sort_desc(ref: Tuple[int, int], ptn: Tuple[int, int]) -> bool:
    return ref[1] < ptn[1] if ref[0] == ptn[0] else ref[0] < ptn[0]


def _quicksort(sort_function, points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    n = len(points)
    if n <= 1:
        return points
    x = points[n//2]
    points.pop(n//2)

    inf, sup = [], []
    for ptn in points:
        if sort_function(x, ptn):
            sup.append(ptn)
        else:
            inf.append(ptn)
    return _quicksort(sort_function, inf) + [x] + _quicksort(sort_function, sup)


# ===========================================================
#                           Process
# ===========================================================
class Sorting(PointProcess):
    """
    Sort points pos with a quicksort algorithm
    Will sort according to the  y desc

    """
    def __init__(self, mode: SortOrder):
        super().__init__()
        self.__mode = mode

    def run(self, points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """
        Launch the sorting process according to the mode

        :param points: the list of pos to be sorted
        :raise NameError: if the mode is incorrect
        """
        self._points = points

        # Start sorting
        print("[Sorting] Starting sorting with mode ("+str(self.__mode)+")")
        if self.__mode is SortOrder.CYCLE:
            self.__sort_cycle()
        elif self.__mode is SortOrder.NORMAL:
            self.__sort_normal()
        else:
            raise NameError("[Sorting] Incorrect Mode ("+str(self.__mode)+")")
        print("[Sorting] Process ended well")

        # Return
        return self._points

    # ===========================================================
    #                           Modes
    # ===========================================================
    def __sort_cycle(self) -> None:
        pos = []
        neg = []
        for ptn in self._points:
            if ptn[1] >= 0:
                pos.append(ptn)
            else:
                neg.append(ptn)
        self._points = _quicksort(_sort_asc, pos)+_quicksort(_sort_desc, neg)

    def __sort_normal(self):
        pass
