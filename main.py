from Processing import *
from Processing.color import Isolator
from Processing.select import Selector, SelOption
import matplotlib.pyplot as plt

from Processing.sort import Sorting, SortOrder, _sort_asc

COLOR = (.29019, .85882, .705882)
COLOR_DIST = .38

proc = Pipeline()
load = ImageLoader("./imgs/c0_redu.png")
load.run()

i = Isolator(COLOR, COLOR_DIST)
i.run(load.get_img())

s = Selector()
s.add_selection(((0, 0), (600, 330)), SelOption.INCLUDE)
s.run(i.get_img())


plt.imshow(load.get_img(), cmap="gray")
plt.imshow(s.get_img(), cmap="gray")
plt.show()

so = Sorting(SortOrder.CYCLE)
so.run([(0, 1)])

print(type(_sort_asc))


