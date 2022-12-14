from itertools import pairwise

input = open("input.txt").readlines()
filled: set[complex] = set()
for edge in [[tuple(map(int, c.split(","))) for c in l.split("->")] for l in input]:
    for (x1, y1), (x2, y2) in pairwise(edge):
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        filled.update(
            complex(r, i) for r in range(x1, x2 + 1) for i in range(y1, y2 + 1)
        )

bottom = max(p.imag for p in filled) + 1
count1 = count2 = 0
old = start = 500 + 0j
offsets = (0 + 1j, -1 + 1j, 1 + 1j)
while start not in filled:
    new = next((old + o for o in offsets if old + o not in filled), old)
    if count1 == 0 and new.imag == bottom - 1:
        count1 = count2
    if new == old or new.imag > bottom:
        filled.add(old)
        count2 += 1
        old = start
    else:
        old = new

print(f"Result 1: {count1}")
print(f"Result 2: {count2}")
