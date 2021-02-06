from abc import *
from typing import Tuple, List
from numpy import ndarray


class Process:
    def __init__(self):
        pass

    @abstractmethod
    def run(self, table: any) -> any:
        """
        Run the process
        """
        pass


class ImageProcess(Process):
    def __init__(self):
        super().__init__()
        self._img = None

    @abstractmethod
    def run(self, img: ndarray) -> ndarray:
        pass

    def get_img(self) -> ndarray:
        """
        Return the processed image or None if run() wasn't trigger once
        """
        return self._img


class PointProcess(Process):
    def __init__(self):
        super().__init__()
        self._points = []

    def run(self, points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        pass

    def get_points(self) -> List[Tuple[int, int]]:
        """
        Return the processed points or None if run() wasn't trigger once
        """
        return self._points
