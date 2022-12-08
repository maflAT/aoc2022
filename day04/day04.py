lines = [l.strip() for l in open("input.txt").readlines()]


def contains(line: str) -> bool:
    startA, endA, startB, endB = (int(n) for e in line.split(",") for n in e.split("-"))
    return startA <= startB and endA >= endB or startA >= startB and endA <= endB


print(sum(contains(line) for line in lines))


def overlaps(line: str) -> bool:
    Astart, Aend, Bstart, Bend = (int(n) for e in line.split(",") for n in e.split("-"))
    return not (Astart > Bend or Aend < Bstart)


print(sum(overlaps(line) for line in lines))
