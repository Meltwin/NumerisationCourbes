from Processing import *
from Processing.color import Isolator
import matplotlib.image as pli
import matplotlib.pyplot as plt

proc = Pipeline()
load = ImageLoader("./imgs/c0_redu.png")
load.run(None)
color = (.29019, .85882, .705882)
dist = .38
i = Isolator(color, dist)
i.run(load.get_img())

plt.imshow(load.get_img(), cmap="gray")
plt.imshow(i.get_img(), cmap="gray")
plt.show()
