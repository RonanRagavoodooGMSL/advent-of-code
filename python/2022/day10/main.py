# Part 1
x = 1
values = [0]
for cmd in open("python/2022/day10/test.txt").read().split("\n"):
    if cmd == "noop":
        values.append(x)
    else:
        _, val = cmd.split()
        values.extend([x, x])
        x += int(val)
# Part 2
print(sum([values[i] * i for i in [20, 60, 100, 140, 180, 220]]))

crt = [["."] * 40 for _ in range(6)]
cycle = 1
for row in crt:
    for i in range(len(row)):
        sprite = [values[cycle] - 1, values[cycle], values[cycle] + 1]
        if i in sprite:
            row[i] = "#"
        cycle += 1
[print("".join(row)) for row in crt]
