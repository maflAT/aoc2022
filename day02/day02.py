OPPONENT = {
    "A": "R",
    "B": "P",
    "C": "S",
}
SELF = {
    "X": "R",
    "Y": "P",
    "Z": "S",
}
POINTS = {
    "PR": 1,  # rock loss
    "SP": 2,  # paper loss
    "RS": 3,  # scissor loss
    "RR": 4,  # rock draw
    "PP": 5,  # paper draw
    "SS": 6,  # scissor draw
    "SR": 7,  # rock win
    "RP": 8,  # paper win
    "PS": 9,  # scissor win
}


def points(input: str) -> int:
    with open(input) as f:
        return sum(
            POINTS[line.strip().translate(str.maketrans({" ": "", **OPPONENT, **SELF}))]
            for line in f
        )


TRANS = {
    "AX": "RS",  # rock loss
    "BX": "PR",  # paper loss
    "CX": "SP",  # scissor loss
    "AY": "RR",  # rock draw
    "BY": "PP",  # paper draw
    "CY": "SS",  # scissor draw
    "AZ": "RP",  # rock win
    "BZ": "PS",  # paper win
    "CZ": "SR",  # scissor win
}


def points2(input: str) -> int:
    with open(input) as f:
        return sum(POINTS[TRANS[line.strip().replace(" ", "")]] for line in f)


print(points("input.txt"))
print(points2("input.txt"))
