pairs = []
with open("python/2022/day2/test.txt") as f:
    for line in f.readlines():
        pair = line.strip().split(" ")
        pairs.append((pair[0], pair[1]))

wins = {"ROCK": "SCISSORS", "PAPER": "ROCK", "SCISSORS": "PAPER"}
symbols = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS",
}
symbol_score = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}

score = 0
for pair in pairs:
    my_symbol = symbols[pair[1]]
    their_symbol = symbols[pair[0]]
    sym = symbol_score[my_symbol]
    if wins[my_symbol] == their_symbol:
        score += sym + 6
    elif my_symbol == their_symbol:
        score += sym + 3
    else:
        score += sym

print(score)
