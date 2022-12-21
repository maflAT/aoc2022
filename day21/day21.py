from time import perf_counter

op_lut = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}
t = perf_counter()
# -------------------------------------- Part 1: ------------------------------------- #
values: dict[str, int] = {}
children: dict[str, tuple[str, str]] = {}
ops: dict[str, str] = {}
monkeys: set[str] = set()
for l in open("input.txt"):
    name, rest = l.split(": ")
    if rest.strip().isdecimal():
        values[name] = int(rest)
    else:
        monkeys.add(name)
        a, op, b = rest.split()
        children[name] = (a, b)
        ops[name] = op
values.pop("humn")
new = None
while (prev := new) != (new := len(monkeys)):
    for m in monkeys.copy():
        if m in values:
            continue
        a, b = children[m]
        if a in values and b in values:
            values[m] = op_lut[ops[m]](values[a], values[b])
            monkeys.remove(m)
# [print(f"{k}: {v}") for k, v in values.items()]
# -------------------------------------- Part 2: ------------------------------------- #
monkeys.add("humn")


def solve_children(parent: str) -> int:
    vp = values[parent]
    if parent == "humn":
        return vp
    ca, cb = children[parent]
    if va := values.get(ca):
        match ops[parent]:
            case "+":
                vb = vp - va
            case "-":
                vb = va - vp
            case "*":
                vb = vp // va
            case "/":
                vb = va // vp
        values[cb] = vb
        return solve_children(cb)
    else:
        vb = values[cb]
        match ops[parent]:
            case "+":
                va = vp - vb
            case "-":
                va = vp + vb
            case "*":
                va = vp // vb
            case "/":
                va = vp * vb
        values[ca] = va
        return solve_children(ca)


c1, c2 = children["root"]
if values.get(c1):
    values[c2] = values[c1]
    res2 = solve_children(c2)
else:
    values[c1] = values[c2]
    res2 = solve_children(c1)

print(f"Result 2: {res2} in {(perf_counter() - t) * 1000:.1f} ms")
