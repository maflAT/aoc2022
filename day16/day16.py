import itertools
import re
import time

t_ = time.perf_counter()
input = open("input.txt").readlines()
pattern = re.compile(r"Valve (\w\w).*rate=(\d+);.*valves* (\w\w(?:, \w\w)*)")
valve_readings = [re.match(pattern, line).groups() for line in input]
connections = {n: c.split(", ") for n, _, c in valve_readings}
rates = {n: int(r) for n, r, _ in valve_readings}

distances: dict[tuple[str, str], int] = {}


def distance(origin: str, dest: str, path: list[str]) -> int:
    if dest == origin:
        return 0
    if d := distances.get((origin, dest)):
        return d
    if dest in connections[origin]:
        distances[(origin, dest)] = 1
        distances[(dest, origin)] = 1
        return 1
    if not (c := [o for o in connections[origin] if o not in path]):
        return 999
    if (d := min(distance(o, dest, path + [origin]) for o in c) + 1) < 999:
        distances[(origin, dest)] = d
        distances[(dest, origin)] = d
    return d


for o, d in itertools.product(connections.keys(), repeat=2):
    distances[o, d] = distance(o, d, [])


def open_valve(here: str, remaining_valves: set[str], t: int) -> int:
    t -= 1
    if t == 0:
        return 0
    p = rates[here] * t
    r = {v for v in remaining_valves - {here} if distances[here, v] < t}
    if not r:
        return p
    return p + max(open_valve(v, r, t - distances[here, v]) for v in r)


t = 31
here = "AA"
valves = {v for v, r in rates.items() if r > 0 and distances[here, v] < t}
res1 = open_valve(here, valves, t)


# print(time.perf_counter() - t)
# -------------------------------------- Part 1 -------------------------------------- #
print(f"Result 1: {res1} in {time.perf_counter() - t_:.3f} s")

# -------------------------------------- Part 2: ------------------------------------- #
# print(f"Result 2: {res2} in {time.perf_counter() - t:.3f} s")
