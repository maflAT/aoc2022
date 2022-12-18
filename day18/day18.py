from itertools import product
from time import perf_counter
import numpy as np

t = perf_counter()
# -------------------------------------- Part 1: ------------------------------------- #
lava = np.full((21, 21, 21), False, bool)
for pos in (tuple(map(int, line.split(","))) for line in open("input.txt")):
    lava[pos] = True
result_1 = sum(np.sum(np.diff(lava, 1, dim, False, False)) for dim in [0, 1, 2])
print(f"Result 1: {result_1} in {(perf_counter() - t) * 1000:.1f} ms")

t = perf_counter()
# -------------------------------------- Part 2: ------------------------------------- #
water = np.full_like(lava, True, bool)
water[1:-1, 1:-1, 1:-1] = False
new = None
while (previous := new) != (new := water.sum()):
    neighbors = [np.roll(water, dir, ax) for dir, ax in product([1, -1], [0, 1, 2])]
    water = ~lava & np.any(neighbors, axis=0)
result_2 = sum(np.sum(np.diff(~water, 1, dim, False, False)) for dim in [0, 1, 2])
print(f"Result 2: {result_2} in {(perf_counter() - t) * 1000:.1f} ms")
