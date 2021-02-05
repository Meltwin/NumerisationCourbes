import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt


class Picture:
    """
    Class for loading pictures from the computer
    """

    def __init__(self, path: str, absolute=False):
        self.__path = path
        self.__absolute = absolute
        self.img = None
        self.load_img()

    def load_img(self) -> None:
        self.img = img.imread(self.__path)

    def show_img(self) -> None:
        plt.imshow(self.img)
        plt.show()

    def get_img(self) -> np.ndarray:
        return self.img


class PictureShow:
    INDEX = 1
    """
    Show in pyplot pictures
    """

    def __init__(self, n: int, p: int, title: str) -> None:
        self.size = [n, p]
        self.index = [0, 0]
        _, self.cases = plt.subplots(n, p)
        plt.figure(PictureShow.INDEX).canvas.set_window_title(title)
        PictureShow.INDEX += 1

    def add_image(self, pict: np.ndarray, title: str, gray=False) -> None:
        elem = None
        if type(self.cases[0]) == np.ndarray:
            elem = self.cases[self.index[0], self.index[1]]
        else:
            elem = self.cases[self.index[0]]
        if gray:
            elem.imshow(pict, cmap="gray")
        else:
            elem.imshow(pict)
        elem.title.set_text(title)
        elem.xaxis.set_visible(False)
        elem.yaxis.set_visible(False)
        self.__increment_index()

    def __increment_index(self):
        self.index[1] += 1
        if self.index[1] >= self.size[0]:
            self.index[0] += 1
            self.index[1] -= self.size[0]


class Isolator:
    def __init__(self, color, dist_max):
        self.color = color
        self.dist_max = dist_max**2

    def isolate(self, img, zone):
        """

        :param img:
        :param zone: [(xmin=1,ymin=1),(xmax,ymax)]
        :return:
        """
        n, m, c = img.shape
        out = np.zeros([n, m])
        for x in range(1,n):
            for y in range(1,m):
                if zone[0][0] <= y <= zone[1][0] and zone[0][1] <= x <= zone[1][1]:
                    dsquare = (self.color[0]-img[x][y][0])**2 + (self.color[1]-img[x][y][1])**2 + (self.color[2]-img[x][y][2])**2
                    if dsquare <= self.dist_max:
                        out[x][y] = 1
        return out


def tri_points(data):
    if len(data) <= 1:
        return data
    m = len(data)//2
    x = data[m]
    data.pop(m)
    Li = []
    Le = []
    for (i, j) in data:
        if x[1]<0:
            if j>0:
                Li.append((i,j))
            elif i>x[0]:
                Li.append((i,j))
            else:
                Le.append((i,j))
        else:
            if j<0:
                Le.append((i,j))
            elif i<x[0]:
                Li.append((i,j))
            else:
                Le.append((i,j))
    return tri_points(Li)+[x]+tri_points(Le)


class PointPicker:
    def __init__(self, origin, vec_x, amount_x, vec_y, amount_y):
        self.origin = origin
        self.vecX = vec_x
        self.vecY = vec_y
        self.amountX = amount_x
        self.amountY = amount_y

    def pick_point(self, img):
        n, m = img.shape
        self.points = []
        for x in range(m):
            for y in range(n):
                if img[y][x] == 1:
                    pos_x = x-self.origin[0]
                    pos_y = y-self.origin[1]
                    proj_x = pos_x*self.vecX[0] + pos_y*self.vecX[1]
                    proj_y = pos_x*self.vecY[0] + pos_y*self.vecY[1]
                    self.points.append((proj_x*self.amountX, proj_y*self.amountY))
        self.points = tri_points(self.points)
        return self.points


class CSVCreator:
    def __init__(self, file):
        self.filename = file

    def write(self, data):
        f = open(self.filename, "w+")
        for (x, y) in data:
            f.write("{0}, {1}\n".format(x, y))
        f.close()
