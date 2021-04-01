from math import ceil, floor


def rectangular(x_min: int, y_min: int, x_max: int, y_max: int):
    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            yield i, j


def un_parallel_grow(margin: int, final: int, ratio: float):
    for x in range(margin, final-margin):
        yield x, floor((x-margin)/ratio)
