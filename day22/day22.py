import re
from itertools import count, zip_longest
from time import perf_counter

t = perf_counter()
input_map, cmds = open("input.txt").read().split("\n\n")
# -------------------------------------- Part 1: ------------------------------------- #
def move(pos: complex, step: complex) -> complex:
    # print(f"{pos = }, {step = }")
    if (target := pos + step) not in grid:
        # print(f"{target = } not in grid")
        while (target := target - step) in grid:
            # print(target)
            pass
        target += step
        # print(f"new {target = }")
    if grid[target] == "#":
        return (target - step) if (target - step) in grid else pos
    if grid[target] == ".":
        return target
    raise ValueError(pos, step)


grid = {
    complex(x, y): char
    for y, line in enumerate(input_map.splitlines())
    for x, char in enumerate(line)
    if char in ".#"
}
move_cmds = [int(n) for n in re.findall(r"\d+", cmds)]
turn_cmds = [-1 if c == "L" else 1 for c in re.findall(r"[LR]", cmds)]
directions = [1 + 0j, 1j, -1 + 0j, -1j]

# print(grid)
# print(list(move_cmds))
# print(list(turn_cmds))

pos = next(p for p in count() if p in grid)
orientation = directions[0]
for steps, turn in zip_longest(move_cmds, turn_cmds, fillvalue=0):
    # print(steps)
    for _ in range(steps):
        pos = move(pos, orientation)
    orientation = directions[(directions.index(orientation) + turn) % 4]
    # print(pos)
res1 = (pos.imag + 1) * 1000 + (pos.real + 1) * 4 + directions.index(orientation)

print(f"Result 1: {res1:.0f} in {(perf_counter() - t) * 1000:.1f} ms")

# -------------------------------------- Part 2: ------------------------------------- #

# print(f"Result 2: {res2} in {(perf_counter() - t) * 1000:.1f} ms")
