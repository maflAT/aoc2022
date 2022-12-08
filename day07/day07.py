from __future__ import annotations


class Directory:
    def __init__(self, name: str, parent: Directory | None) -> None:
        self.name = name
        self.parent = parent or self
        self.subs: dict[str, Directory] = {}
        self.files: dict[str, int] = {}

    def size(self) -> int:
        return sum(d.size() for d in self.subs.values()) + sum(self.files.values())

    def recursive_subs(self) -> set[Directory]:
        return {self}.union(*(sub.recursive_subs() for sub in self.subs.values()))


input = open("input.txt").readlines()

cwd = root = Directory("/", None)
for line in input:
    match line.split():
        case ["$", "cd", "/"]:
            cwd = root
        case ["$", "cd", ".."]:
            cwd = cwd.parent
        case ["$", "cd", sub]:
            cwd = cwd.subs.setdefault(sub, Directory(sub, cwd))
        case ["dir", sub]:
            cwd.subs[sub] = Directory(sub, cwd)
        case [size, file_name] if size.isdecimal():
            cwd.files[file_name] = int(size)

part1_result = sum(d.size() for d in root.recursive_subs() if d.size() <= 100000)
print(f"Result 1: {part1_result}")

required = root.size() + 30000000 - 70000000
part2_result = min(d.size() for d in root.recursive_subs() if d.size() >= required)
print(f"Result 2: {part2_result}")
