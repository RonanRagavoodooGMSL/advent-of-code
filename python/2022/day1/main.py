print(max([sum([int(i) for i in x.split("\n")])for x in open("python/2022/day1/test.txt").read().split("\n\n")]))

print(sum(sorted([sum([int(i) for i in x.split("\n")])for x in open("python/2022/day1/test.txt").read().split("\n\n")])[-3:]))