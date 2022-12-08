input = open("input.txt").read()
print(next(i + 4 for i in range(len(input)) if len({*input[i : i + 4]}) == 4))
print(next(i + 14 for i in range(len(input)) if len({*input[i : i + 14]}) == 14))
