"""
    CSCI 3302 Data Structures & Algorithms 2 Modified Algorithm
    Name        : Muhammad Hadif Bin Mohd Hatta (hdfhtt)
    Matric no   : 2114589
    Language/IDE: Python 3.9 / PyCharm 2022.3
    Date        : 23/01/2023
"""

from collections import namedtuple
import math


# Flight Time (modified algorithm)
def flight_time(n, w, c, wv):
    w_all = sum(w)

    for _ in next(c):
        # todo: flight_time[1 << (next - 1)][next] <- flight_time(depot_to_next)
        w[1 << (n - 1)] = w_all - next(w)

    for _ in [0, 1, 2, (2 ^ n - 1)]:
        for _ in next(c):
            if next(c) is not next(c).isVisited:
                for _ in prev(c):
                    if prev(c) is prev(c).isVisited:
                        # todo: flight_time[visited|(1 << (next - 1))][Next] <- min(flight_time[visited][previous]
                        #  + flight_time(prev_to_next), flight_time[visited|(1 << (next - 1))][next])
                        c.isVisited = True
                        w[1 << (n - 1)] = w.isVisited - next(w)

    min_time = math.inf

    for _ in prev(c):
        # todo: min_time = min(FT[2N-1][Previous] + flight_time(Previous to depot), min_time)
        print(None)


# helper function to iter backward
def prev(self):
    self.index -= 1
    if self.index < 0:
        raise StopIteration
    return self.collection[self.index]


if __name__ == '__main__':
    coords = namedtuple("Coords", ['x', 'y'])

    c_payloads = [10, 20, 15, 5]
    c_coords = [coords[0.0, 0.0], coords[12.5, 33.1], coords[24.9, 44.1], coords[11.5, 30.6]]

    flight_time(3, c_payloads, iter(c_coords), 0)
