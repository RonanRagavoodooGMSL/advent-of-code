with open("python/2022/day5/test.txt") as f:
    data = f.read().split("\n\n")
    rows = [
        [y.strip("[] ") for y in x if not y.isspace()]
        for x in zip(
            *[
                [line[i : i + 4] for i in range(0, len(line), 4)]
                for line in [x for x in data[0].split("\n")][:-1]
            ]
        )
    ]
    for op in [[int(i) for i in x.split() if i.isdigit()] for x in data[1].split("\n")]:
        rows[op[2] - 1] = list(reversed(rows[op[1] - 1][: op[0]])) + rows[op[2] - 1]
        rows[op[1] - 1] = rows[op[1] - 1][op[0] :]

    print("".join([x[0] for x in rows]))
