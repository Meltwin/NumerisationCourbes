from typing import Tuple
from Processing.process import Process, ImageProcess

import matplotlib.image as pli
import numpy as np


class Pipeline:
	"""
	Create a pipeline from image processing
	"""
	def __init__(self):
		self.process = []
		
	def reg_proc(self, proc: Process) -> None:
		"""
		Add a process into the pipeline
		"""
		self.process.append(proc)
	
	def run_all(self) -> None:
		"""
		Run all the registered process
		"""
		img = None
		for proc in self.process:
			proc.run()


class ImageLoader(ImageProcess):
	"""
	Load an image from the disk into a numpy ndarray 
	"""
	def __init__(self, path: str) -> None:
		super().__init__()
		self.__path = path
		
	def run(self, _=None) -> np.ndarray:
		self._img = pli.imread(self.__path)
		print("[Loading] Loaded file", end="\n\n")
		return self._img


def table_course_gene(x_max: int, y_max: int, x_min: int = 0, y_min: int = 0) -> Tuple[int, int]:
	"""
	Make a rectangle pos generator between the two given corners
	"""
	for x in range(x_min, x_max):
		for y in range(y_min, y_max):
			yield x, y
