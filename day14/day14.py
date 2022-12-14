from itertools import pairwise, product

input = open("input.txt").readlines()
filled: set[tuple[int, int]] = set()
for e in [[tuple(map(int, c.split(","))) for c in l.split("->")] for l in input]:
    for (x1, y1), (x2, y2) in pairwise(e):
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        filled.update(product(range(x1, x2 + 1), range(y1, y2 + 1)))

bottom = max(y for _, y in filled)
count1 = count2 = 0
old = start = (500, 0)
while start not in filled:
    x, y = old[0], old[1] + 1
    new = next(((x + dx, y) for dx in [0, -1, 1] if (x + dx, y) not in filled), old)
    if count1 == 0 and new[1] == bottom:
        count1 = count2
    if new == old or new[1] > bottom:
        filled.add(old)
        count2 += 1
        old = start
    else:
        old = new

print(f"Result 1: {count1}")
print(f"Result 2: {count2}")
# for y in range(bottom + 1):
#     for x in range(490, 510):
#         print("#" if (x, y) in filled else ".", end="")
#     print()
