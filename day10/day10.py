input = open("input.txt").readlines()

values = [1]
for cmd in input:
    values.append(values[-1])
    if cmd.startswith("addx"):
        values.append(values[-1] + int(cmd.split()[1]))
res1 = sum(values[i - 1] * i for i in [20, 60, 100, 140, 180, 220])

res2 = "\n".join(
    "".join(
        "#" if abs(value - i) <= 1 else " "
        for i, value in enumerate(values[i : min(i + 40, len(values))])
    )
    for i in range(0, len(values), 40)
)

print(f"Result 1: {res1}")
print(f"Result 2:\n{res2}")
