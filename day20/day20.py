from itertools import chain, repeat
from time import perf_counter

# -------------------------------------- Part 1: ------------------------------------- #
t = perf_counter()
lut = {tag: num for tag, num in enumerate(int(l) for l in open("input.txt"))}
tags = list(lut)
for tag, n in lut.items():
    tags.pop(idx := tags.index(tag))
    tags.insert((idx + n) % len(tags), tag)
nums = [lut[t] for t in tags]
res1 = sum([nums[(nums.index(0) + o) % len(nums)] for o in [1000, 2000, 3000]])
print(f"Result 1: {res1} in {(perf_counter() - t) * 1000:.0f} ms")

# -------------------------------------- Part 2: ------------------------------------- #
t = perf_counter()
lut = {tag: n * 811_589_153 for tag, n in enumerate(int(l) for l in open("input.txt"))}
tags = list(lut)
for tag, n in chain.from_iterable(repeat(lut.items(), 10)):
    tags.pop(idx := tags.index(tag))
    tags.insert((idx + n) % len(tags), tag)
nums = [lut[t] for t in tags]
res2 = sum(nums[(nums.index(0) + o) % len(nums)] for o in [1000, 2000, 3000])
print(f"Result 2: {res2} in {(perf_counter() - t) * 1000:.0f} ms")
