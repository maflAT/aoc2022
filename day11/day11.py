import math
import operator
from dataclasses import dataclass, field
from typing import IO, Callable


@dataclass
class Monkey:
    items: list[int]
    op: Callable[[int], int]
    divisor: int
    on_pass: int
    on_fail: int
    insp_ct: int = field(default=0)

    def inspect(self, part_2: bool = False) -> None:
        while self.items:
            wl = self.op(self.items.pop())
            wl = wl % lcm if part_2 else wl // 3
            target = self.on_pass if wl % self.divisor == 0 else self.on_fail
            monkeys[target].items.append(wl)
            self.insp_ct += 1


def parse(fh: IO[str]) -> list[Monkey]:
    monkeys: list[Monkey] = []
    while True:
        try:
            next(fh)  # skip header
            m = Monkey(
                items=[int(n) for n in next(fh).split(":")[1].split(",")],
                op=parse_op(next(fh)),
                divisor=int(next(fh).split()[-1]),
                on_pass=int(next(fh).split()[-1]),
                on_fail=int(next(fh).split()[-1]),
            )
            monkeys.append(m)
            next(fh)  # skip empty line
        except StopIteration:
            break
    return monkeys


def parse_op(line: str) -> Callable[[int], int]:
    op_sym, op_val = line.split("=")[1].split()[1:]
    op = operator.add if op_sym == "+" else operator.mul
    return (lambda n: op(n, n)) if op_val == "old" else (lambda n: op(n, int(op_val)))


# -------------------------------------- Part 1: ------------------------------------- #
with open("input.txt") as fh:
    monkeys = parse(fh)
for _ in range(20):
    for m in monkeys:
        m.inspect()
scores = sorted(m.insp_ct for m in monkeys)
print(f"Result 1: {scores[-1] * scores[-2]}")

# -------------------------------------- Part 2 -------------------------------------- #
with open("input.txt") as fh:
    monkeys = parse(fh)
    lcm = math.lcm(*(m.divisor for m in monkeys))
for i in range(10000):
    for m in monkeys:
        m.inspect(part_2=True)
scores = sorted(m.insp_ct for m in monkeys)
print(f"Result 2: {scores[-1] * scores[-2]}")
