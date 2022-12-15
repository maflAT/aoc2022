import re
from typing import Iterable


class Reading:
    __slots__ = ["sx", "sy", "bx", "by", "rx", "ry", "range"]

    def __init__(self, sx: str, sy: str, bx: str, by: str) -> None:
        self.sx = int(sx)
        self.sy = int(sy)
        self.bx = int(bx)
        self.by = int(by)
        self.rx = abs(self.bx - self.sx)
        self.ry = abs(self.by - self.sy)
        self.range = self.rx + self.ry

    def row_coverage(self, row: int) -> tuple[int, int] | None:
        if abs(row - self.sy) > self.range:
            return None
        hor_range = self.range - abs(row - self.sy)
        return self.sx - hor_range, self.sx + hor_range


def merge_ranges(ranges: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    sr_iter = iter(sorted(ranges))
    cur_low, cur_high = next(sr_iter)
    res: list[tuple[int, int]] = []
    for low, high in sr_iter:
        if low <= cur_high + 1:
            cur_high = max(cur_high, high)
        else:
            res.append((cur_low, cur_high))
            cur_low, cur_high = low, high
    res.append((cur_low, cur_high))
    return res


input = open("input.txt").read()
pattern = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
readings = list(Reading(*m) for m in re.findall(pattern, input))

# -------------------------------------- Part 1: ------------------------------------- #
row = 2_000_000
beacons = len({(r.bx, r.by) for r in readings if r.by == row})
rc = merge_ranges(r.row_coverage(row) for r in readings if r.row_coverage(row))
res1 = sum(h - l + 1 for l, h in rc) - beacons
print(f"Result 1: {res1}")

# -------------------------------------- Part 2: ------------------------------------- #
for row in range(4_000_000):
    rc = merge_ranges(r.row_coverage(row) for r in readings if r.row_coverage(row))
    if len(rc) == 1:
        low, high = rc[0]
        if low > 0 or high < 4_000_000:
            res2 = (0 if low > 0 else high + 1) * 4_000_000 + row
            break
    else:
        res2 = (rc[0][1] + 1) * 4_000_000 + row
        break
print(f"Result 2: {res2}")
