from time import perf_counter

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}
t = perf_counter()
# -------------------------------------- Part 1: ------------------------------------- #
values: dict[str, int] = {}
operands: dict[str, tuple[str, str]] = {}
ops: dict[str, str] = {}
monkeys: set[str] = set()
for l in open("input.txt"):
    name, rest = l.split(": ")
    if rest.strip().isdecimal():
        values[name] = int(rest)
    else:
        monkeys.add(name)
        a, op, b = rest.split()
        operands[name] = (a, b)
        ops[name] = op
while monkeys:
    for m in monkeys.copy():
        if m in values:
            continue
        a, b = operands[m]
        if a in values and b in values:
            values[m] = operations[ops[m]](values[a], values[b])
            monkeys.remove(m)
res1 = values["root"]
print(f"Result 1: {res1} in {(perf_counter() - t) * 1000:.1f} ms")

# t = perf_counter()
# -------------------------------------- Part 2: ------------------------------------- #

# print(f"Result 2: {res2} in {(perf_counter() - t) * 1000:.1f} ms")
