# Part 1
print(sum([ord(x[1]) - 87 + ((((ord(x[1]) - ord(x[0])) + 2) % 3) * 3) for x in [line.strip().split(" ") for line in open("python/2022/day2/test.txt").readlines()]]))
# Part 2
print(sum([((ord(x[1]) - 88) * 3) + (((ord(x[0]) - 65) + ord(x[1]) - 89) % 3) + 1 for x in [line.strip().split(" ") for line in open("python/2022/day2/test.txt").readlines()]]))