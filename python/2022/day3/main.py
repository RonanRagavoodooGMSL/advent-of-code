import string

# Part 1
print(sum([{k: v for (k, v) in list(zip(list(string.ascii_lowercase + string.ascii_uppercase),[priority for priority in range(1, 53)]))}[x] for x in [list(set([x for x in pair[0] if x in pair[1]]))[0] for pair in [(container[:int(len(container) / 2)], container[int(len(container) / 2):]) for container in [line.strip() for line in open("python/2022/day3/test.txt").readlines()]]]]))

# Part 2
print((lambda rucksacks : (sum([[{k: v for (k, v) in list(zip(list(string.ascii_lowercase + string.ascii_uppercase),[priority for priority in range(1, 53)]))}[i] for i in group[0] if i in group[1] and i in group[2]][0] for group in [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]])))([set(x.strip()) for x in open("python/2022/day3/test.txt").readlines()]))

