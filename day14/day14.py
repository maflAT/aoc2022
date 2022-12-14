from itertools import pairwise, product
from typing import Iterable

input = [l.strip() for l in open("input.txt").readlines()]
rock_edges = [
    [tuple(map(int, c.split(","))) for c in l.replace("->", "").split()] for l in input
]
filled: set[tuple[int, int]] = set()


def fill(p1: tuple[int, int], p2: tuple[int, int]) -> Iterable[tuple[int, int]]:
    x1, x2 = sorted([p1[0], p2[0]])
    y1, y2 = sorted([p1[1], p2[1]])
    return product(range(x1, x2 + 1), range(y1, y2 + 1))


def move(pos: tuple[int, int]) -> tuple[int, int]:
    x, y = pos[0], pos[1] + 1
    return next(((x + o, y) for o in [0, -1, 1] if (x + o, y) not in filled), pos)


for e in rock_edges:
    for c1, c2 in pairwise(e):
        filled.update(fill(c1, c2))
filled2 = filled.copy()

bottom = max(y for _, y in filled)
count = 0
pos = (500, 0)
while pos[1] < bottom:
    if (new := move(pos)) == pos:
        filled.add(pos)
        count += 1
        pos = (500, 0)
    else:
        pos = new

print(f"Result 1: {count}")

# -------------------------------------- Part 2: ------------------------------------- #
filled = filled2
bottom += 2
count = 0
pos = (500, 0)
while True:
    if (new := move(pos)) == pos:
        filled.add(pos)
        count += 1
        if new == (500, 0):
            break
        pos = (500, 0)
    elif new[1] == bottom:
        filled.add(new)
        pos = (500, 0)
    else:
        pos = new

# for y in range(bottom + 1):
#     for x in range(490, 510):
#         print("#" if (x, y) in filled else ".", end="")
#     print()
print(f"Result 2: {count}")
