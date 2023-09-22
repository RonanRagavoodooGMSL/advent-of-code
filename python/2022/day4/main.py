# Part 1
print(len([0 for pair1, pair2 in [(pair1.split("-"), pair2.split("-")) for pair1, pair2 in [line.strip().split(",") for line in open("python/2022/day4/test.txt")]] if (set([x for x in range(int(pair1[0]), int(pair1[1]) + 1)]).issubset(set([y for y in range(int(pair2[0]), int(pair2[1]) + 1)]))) or (set([x for x in range(int(pair2[0]), int(pair2[1]) + 1)]).issubset(set([y for y in range(int(pair1[0]), int(pair1[1]) + 1)])))]))

# Part 2
print(len([0 for pair1, pair2 in [(pair1.split("-"), pair2.split("-")) for pair1, pair2 in [line.strip().split(",") for line in open("python/2022/day4/test.txt")]] if (set([x for x in range(int(pair1[0]), int(pair1[1]) + 1)]) & (set([y for y in range(int(pair2[0]), int(pair2[1]) + 1)])))]))
