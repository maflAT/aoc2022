def max_calories(input: str) -> int:
    max_calories = 0
    current_calories = 0
    with open(input) as f:
        for line in f:
            if line == "\n":
                current_calories = 0
                continue
            current_calories += int(line)
            max_calories = max(max_calories, current_calories)
    return max_calories


def top3(input: str) -> int:
    elf_calories = []
    current_calories = 0
    with open(input) as f:
        for line in f:
            if line == "\n":
                elf_calories.append(current_calories)
                current_calories = 0
                continue
            current_calories += int(line)
    return sum(sorted(elf_calories, reverse=True)[:3])


print(max_calories("input.txt"))
print(top3("input.txt"))
