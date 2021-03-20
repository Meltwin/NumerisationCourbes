from typing import Tuple, List

from Processing.process import PointProcess


class CSVExport(PointProcess):
    def __init__(self, filepath: str):
        super().__init__()
        self.__filepath = filepath

    def run(self, points: List[Tuple[int, int]]) -> None:
        print("[  IO   ] Starting exporting in CSV in file \""+self.__filepath+"\"")
        handle = open(self.__filepath, "w+")
        for (x, y) in points:
            handle.write("{0}, {1}\n".format(x, y))
        handle.close()
        print("[  IO   ] Finished exporting in CSV !")
