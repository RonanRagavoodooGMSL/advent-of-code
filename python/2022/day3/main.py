import string

lwr = string.ascii_lowercase
upp = string.ascii_uppercase
scores = {}

for i in range(1, 27):
    scores[lwr[i - 1]] = i
for j in range(27, 53):
    scores[upp[j - 27]] = j

# rucksacks = []
# commons = []
# with open("python/2022/day3/test.txt") as f:
#     for line in f.readlines():
#         items = line.strip()
#         container_length = int(len(items) / 2)
#         rucksacks.append((items[:container_length], items[container_length:]))

# for pair in rucksacks:
#     commons.extend(set([x for x in pair[0] if x in pair[1]]))

# print(sum([scores[x] for x in commons]))

with open("python/2022/day3/test.txt") as f:
    # for group in f.read().split("\r\n\r\n"):
    #     print(group)
    x = [set(x.strip()) for x in f.readlines()]
    print([x[i : i + 3] for i in range(0, len(x), 3)])
