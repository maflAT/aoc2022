import re
import time
from itertools import chain, product
from typing import Iterable

t = time.perf_counter()


class Reading:
    def __init__(self, sx: str, sy: str, bx: str, by: str) -> None:
        self.sx = int(sx)
        self.sy = int(sy)
        self.bx = int(bx)
        self.by = int(by)
        self.rx = abs(self.bx - self.sx)
        self.ry = abs(self.by - self.sy)
        self.range = self.rx + self.ry

    def __lt__(self, other: "Reading") -> bool:
        return self.range < other.range

    def covers(self, x: int, y: int) -> bool:
        return abs(x - self.sx) + abs(y - self.sy) <= self.range

    def rim(self) -> Iterable[tuple[int, int]]:
        return chain(
            *[
                zip(
                    range(self.sx, self.sx + a * (self.range + 2), a),
                    reversed(range(self.sy, self.sy + b * (self.range + 2), b)),
                )
                for a, b in product((1, -1), repeat=2)
            ]
        )


input = open("input.txt").read()
pattern = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
readings = sorted((Reading(*m) for m in re.findall(pattern, input)), reverse=True)

# -------------------------------------- Part 1: ------------------------------------- #
row = 2_000_000
beacons = len({(r.bx, r.by) for r in readings if r.by == row})
ranges = sorted(
    (r.sx - (hr := r.range - abs(row - r.sy)), r.sx + hr)
    for r in readings
    if abs(row - r.sy) <= r.range
)

cur_low, cur_high = ranges[0]
coverage = 0
for low, high in ranges[1:]:
    if low <= cur_high + 1:
        cur_high = max(cur_high, high)
    else:
        coverage += cur_high - cur_low + 1
        cur_low, cur_high = low, high
coverage += cur_high - cur_low + 1
res1 = coverage - beacons
print(f"Result 1: {res1} in {time.perf_counter() - t:.3f} s")

# -------------------------------------- Part 2: ------------------------------------- #
res2 = next(
    x * 4_000_000 + y
    for r in reversed(readings)
    for x, y in r.rim()
    if not any(r_.covers(x, y) for r_ in readings)
    and 0 <= x <= 4_000_000
    and 0 <= y <= 4_000_000
)
print(f"Result 2: {res2} in {time.perf_counter() - t:.3f} s")
