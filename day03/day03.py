def duplicate(items: str) -> str:
    comp1 = set(items[: len(items) // 2])
    comp2 = set(items[len(items) // 2 :])
    return (comp1 & comp2).pop()


def prio(char: str) -> int:
    offset = 96 if ord(char) >= 97 else 38
    return ord(char) - offset


def sum_priorities(input: str) -> int:
    with open(input) as f:
        return sum(prio(duplicate(rucksack.strip())) for rucksack in f)


def find_badge(rucksacks: list[str]) -> str:
    sets = (set(r) for r in rucksacks)
    return set.intersection(*sets).pop() if sets else ""


with open("input.txt") as f:
    badges = []
    rucksack = []
    for line in f:
        rucksack.append(line.strip())
        if len(rucksack) == 3:
            badges.append(find_badge(rucksack))
            rucksack = []

print(sum_priorities("input.txt"))
print(sum(prio(b) for b in badges))
