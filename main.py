import matplotlib.pyplot as plt

from Processing import *
from Processing.color import *
from Processing.select import *
from Processing.sort import *
from Processing.io import *

COLOR = (.29019, .85882, .705882)
COLOR_DIST = .38

# Image Process
load = ImageLoader("./imgs/c0_redu.png")
load.run()

i = Isolator(COLOR, COLOR_DIST)
i.run(load.get_img())

s = Selector()
s.add_selection(((0, 0), (600, 330)), SelOption.INCLUDE)
s.run(i.get_img())

# Point Process
pt = ImageToPoint()
pt.run(s.get_img())

sort = Sorting(SortOrder.CYCLE)
sort.run(pt.get_points())

expo = CSVExport("./out/c0.csv")
expo.run(sort.get_points())

plt.imshow(load.get_img(), cmap="gray")
plt.imshow(s.get_img(), cmap="gray")
plt.show()


def getXY() -> Tuple[List[int], List[int]]:
    X, Y = [], []
    for (x, y) in sort.get_points():
        X.append(x)
        Y.append(y)
    return X, Y


X, Y = getXY()
plt.plot(X, Y)
plt.show()

