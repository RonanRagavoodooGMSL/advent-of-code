data = open("python/2022/day5/test.txt").read().split("\n\n")
part1 = [[y.strip("[] ") for y in x if not y.isspace()]for x in zip(*[[line[i : i + 4] for i in range(0, len(line), 4)]for line in [x for x in data[0].split("\n")][:-1]])]
part2 = part1.copy()

for op in [[int(i) for i in x.split() if i.isdigit()] for x in data[1].split("\n")]:
    part1[op[2] - 1] = list(reversed(part1[op[1] - 1][: op[0]])) + part1[op[2] - 1]
    part1[op[1] - 1] = part1[op[1] - 1][op[0] :]
    part2[op[2] - 1] = part2[op[1] - 1][: op[0]] + part2[op[2] - 1]
    part2[op[1] - 1] = part2[op[1] - 1][op[0] :]

print("".join([x[0] for x in part1 if x]), "".join([x[0] for x in part2 if x]), sep="\n")
