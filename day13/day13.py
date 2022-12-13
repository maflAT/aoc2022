from itertools import zip_longest


def is_ordered(left, right) -> bool | None:
    if isinstance(left, int) and isinstance(right, int):
        return None if left == right else left < right
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    for l, r in zip_longest(left, right, fillvalue=None):
        if l is None:
            return True
        if r is None:
            return False
        if (o := is_ordered(l, r)) is not None:
            return o
    return None


input = open("input.txt").read()
input_pairs = [[eval(l.strip()) for l in p.split()] for p in input.split("\n\n")]

ordered = [is_ordered(pair[0], pair[1]) for pair in input_pairs]
res1 = sum(i for i, p in enumerate(ordered, 1) if p)
print(f"Result 1: {res1}")
# print(f"Result 2:\n{res2}")
