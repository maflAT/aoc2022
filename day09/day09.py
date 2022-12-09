class Knot:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def coords(self) -> tuple[int, int]:
        return self.x, self.y

    def move(self, direction: str) -> None:
        if direction == "L":
            self.x -= 1
        elif direction == "R":
            self.x += 1
        elif direction == "U":
            self.y -= 1
        elif direction == "D":
            self.y += 1

    def follow(self, leader: "Knot") -> None:
        if abs(leader.x - self.x) > 1 or abs(leader.y - self.y) > 1:
            if leader.x - self.x > 0:
                self.x += 1
            elif leader.x - self.x < 0:
                self.x -= 1
            if leader.y - self.y > 0:
                self.y += 1
            elif leader.y - self.y < 0:
                self.y -= 1


def trace_rope(commands: list[str], rope_length: int) -> set[tuple[int, int]]:
    rope = [Knot() for _ in range(rope_length)]
    head, tail = rope[0], rope[-1]
    visited = {tail.coords()}
    for line in commands:
        direction, steps = line.split()
        for _ in range(int(steps)):
            head.move(direction)
            for i in range(1, len(rope)):
                rope[i].follow(rope[i - 1])
            visited.add(tail.coords())
    return visited


input = open("input.txt").readlines()
print(f"Result 1: {len(trace_rope(input, 2))}")
print(f"Result 2: {len(trace_rope(input, 10))}")
