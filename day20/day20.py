from itertools import product

# -------------------------------------- Part 1: ------------------------------------- #
lut = {tag: num for tag, num in enumerate(int(l) for l in open("input.txt"))}
length = len(lut) - 1
tags = list(lut.keys())
for tag, num in lut.items():
    idx = tags.index(tag)
    del tags[idx]
    tags.insert((idx + num) % length, tag)
nums = [lut[t] for t in tags]
res1 = sum([nums[(nums.index(0) + o) % len(nums)] for o in [1000, 2000, 3000]])
print(f"Result 1: {res1}")

# -------------------------------------- Part 2: ------------------------------------- #
key = 811_589_153
lut = {tag: num * key for tag, num in enumerate(int(l) for l in open("input.txt"))}
tags = list(lut.keys())
for _, (tag, num) in product(range(10), lut.items()):
    idx = tags.index(tag)
    del tags[idx]
    tags.insert((idx + num) % length, tag)
nums = [lut[t] for t in tags]
res2 = sum([nums[(nums.index(0) + o) % len(nums)] for o in [1000, 2000, 3000]])
print(f"Result 2: {res2}")
