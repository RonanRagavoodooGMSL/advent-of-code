import json

part1 = [x.split("\n") for x in open("python/2022/day13/test.txt").read().split("\n\n")]
part2 = [
    json.loads(x)
    for x in open("python/2022/day13/test.txt").read().replace("\n\n", "\n").split("\n")
]
part2.extend([[[2]], [[6]]])


def check_right_input(pair1, pair2):
    for j in range(len(pair2)):
        if j >= len(pair1):
            return True
        if isinstance(pair1[j], int) and isinstance(pair2[j], int):
            if pair1[j] != pair2[j]:
                return pair1[j] < pair2[j]
        if isinstance(pair1[j], list) and isinstance(pair2[j], list):
            res = check_right_input(pair1[j], pair2[j])
            if res is not None:
                return res
        if isinstance(pair1[j], int) and isinstance(pair2[j], list):
            res = check_right_input([pair1[j]], pair2[j])
            if res is not None:
                return res
        if isinstance(pair1[j], list) and isinstance(pair2[j], int):
            res = check_right_input(pair1[j], [pair2[j]])
            if res is not None:
                return res
    if len(pair2) < len(pair1):
        return False
    return None


# Part 1
print(sum([i + 1 for i in range(len(part1)) if check_right_input(json.loads(part1[i][0]), json.loads(part1[i][1]))]))
# Part 2
i = 1
while i < len(part2):
    j = i
    while j > 0 and check_right_input(part2[j - 1], part2[j]) is False:
        tmp = part2[j]
        part2[j] = part2[j - 1]
        part2[j - 1] = tmp
        j -= 1
    i += 1

print((part2.index([[2]]) + 1) * (part2.index([[6]]) + 1))
