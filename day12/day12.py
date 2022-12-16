import time
from collections import deque

coord = tuple[int, int]
heights: dict[coord, int] = {}
paths: dict[coord, list[coord]] = {}
input = [l.strip() for l in open("input.txt").readlines()]
h, w = len(input), len(input[0])


def neighbors(pos: coord) -> list[coord]:
    x, y = pos
    return [
        (min(w - 1, x + 1), y),
        (x, min(h - 1, y + 1)),
        (max(x - 1, 0), y),
        (x, max(y - 1, 0)),
    ]


for y, line in enumerate(input):
    for x, c in enumerate(line):
        if c == "S":
            start = (x, y)
            c = "a"
        elif c == "E":
            end = (x, y)
            c = "z"
        heights[(x, y)] = ord(c) - 97


def visit(here: coord, path: list[coord]) -> None:
    if here in paths:
        return
    paths[here] = path.copy()
    path.append(here)
    if here == end:
        return
    for n in neighbors(here):
        if n not in paths and (heights[n] <= heights[here] + 1):
            visits.append((n, path.copy()))


t = time.perf_counter()
visits = deque()
visits.append((start, []))
while visits:
    pos, path = visits.popleft()
    visit(pos, path)
print(f"Result 1: {len(paths[end])}")

# -------------------------------------- Part 2 -------------------------------------- #
shortest = list(reversed(paths[end]))
paths = {}
paths[start] = shortest


def backtrace(here: coord, path: list[coord]):
    # print(here)
    global shortest
    if here in paths or len(path) >= len(shortest):
        return
    paths[here] = path.copy()
    if heights[here] == 0:
        shortest = path
        return
    path.append(here)
    for n in neighbors(here):
        if heights[n] >= heights[here] - 1:
            visits.append((n, path.copy()))


visits.append((end, []))
while visits:
    pos, path = visits.popleft()
    backtrace(pos, path)

print(f"Result 2: {len(shortest)}")
print(time.perf_counter() - t)
