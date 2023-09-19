res = 0

with open("python/2022/day4/test.txt") as f:
    for line in f.readlines():
        pair1, pair2 = line.strip().split(",")
        if (
            set([x for x in range(int(pair1[0]), int(pair1[2]) + 1)]).issubset(
                set([y for y in range(int(pair2[0]), int(pair2[2]) + 1)])
            )
        ) or (
            set([x for x in range(int(pair2[0]), int(pair2[2]) + 1)]).issubset(
                set([y for y in range(int(pair1[0]), int(pair1[2]) + 1)])
            )
        ):
            print(pair1, pair2)
            res += 1

print(res)
