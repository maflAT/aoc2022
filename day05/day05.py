import re

input_ = open("input.txt").read()


def parse(input: str) -> tuple[list[list[str]], list[tuple[int, int, int]]]:
    arrangement, instructions = (part.split("\n") for part in input.split("\n\n"))
    stacks: list[list[str]] = [[] for _ in arrangement[0][1::4]]
    for line in reversed(arrangement[:-1]):
        for i, char in enumerate(line[1::4]):
            if char != " ":
                stacks[i].append(char)

    pattern = re.compile(r"move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)")
    commands = [map(int, re.match(pattern, line).groups()) for line in instructions]
    return stacks, commands


stacks, commands = parse(input_)
for count, src, dest in commands:
    for _ in range(count):
        stacks[dest - 1].append(stacks[src - 1].pop())

print(f'Top crates: {"".join(s[-1] for s in stacks)}')

stacks, commands = parse(input_)
for count, src, dest in commands:
    stacks[dest - 1].extend(stacks[src - 1][-count:])
    del stacks[src - 1][-count:]

print(f'Top crates: {"".join(s[-1] for s in stacks)}')
