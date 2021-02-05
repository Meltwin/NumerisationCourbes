from abc import *
import matplotlib.image as pli
import numpy as np


class Process:
	def __init__(self):
		self._img = None

	@abstractmethod
	def run(self, img):
		"""
		Run the process 
		"""
		pass

	def get_img(self):
		"""
		Return the processed image or None if the run wasn't run
		"""
		return self._img


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
	
	def run_all(self):
		"""
		Run all the registered process
		"""
		img = None
		for proc in self.process:
			proc.run()


class ImageLoader(Process):
	"""
	Load an image from the disk into a numpy ndarray 
	"""
	def __init__(self, path: str):
		super().__init__()
		self.__path = path
		
	def run(self, img=None) -> np.ndarray:
		self._img = pli.imread(self.__path)
		return self._img
