input = open("input.txt").readlines()

forest = [[int(t) for t in row.strip()] for row in input]
h, w = len(forest), len(forest[0])

vis_count = 0
for x in range(w):
    col = [forest[i][x] for i in range(h)]
    for y in range(h):
        row = forest[y]
        this = forest[y][x]
        vis_count += (
            all(t < this for t in row[:x])
            or all(t < this for t in row[x + 1 :])
            or all(t < this for t in col[:y])
            or all(t < this for t in col[y + 1 :])
        )

high_score = 0
for x in range(w):
    col = [forest[i][x] for i in range(h)]
    for y in range(h):
        row = forest[y]
        this = row[x]
        dist_l = next((d for d in range(1, x) if row[x - d] >= this), x)
        dist_r = next((d for d in range(1, w - x) if row[x + d] >= this), w - x - 1)
        dist_u = next((d for d in range(1, y) if col[y - d] >= this), y)
        dist_d = next((d for d in range(1, h - y) if col[y + d] >= this), h - y - 1)
        high_score = max(high_score, dist_l * dist_r * dist_u * dist_d)

print(f"Day 8 - Result 1: {vis_count}")
print(f"Day 8 - Result 2: {high_score}")
