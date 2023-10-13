import math

monkey_items = []
operations = []
tests = []
choices = []


def operation(i, old):
    old = int(old)
    return eval(operations[i])


for monkey in open("python/2022/day11/test.txt").read().split("\n\n"):
    data = monkey.split("\n")
    inv = [int(x) for x in data[1].strip("Starting items: ").split(",")]
    monkey_items.append(inv)
    num_inspections = len(monkey)
    operations.append(data[2].replace("Operation: new = ", "").strip())
    tests.append(int("".join([s for s in data[3] if s.isdigit()])))
    choices.append(((int(data[4][-1])), int(data[5][-1])))

inspections = [0 for _ in range(len(tests))]
common_mod = 1
for x in tests:
    common_mod *= x


# for _ in range(20):
#     for i in range(len(tests)):
#         while monkey_items[i]:
#             item = monkey_items[i].pop(0)
#             item = operation(i, item)
#             item = math.floor(item / 3)
#             if item % tests[i] == 0:
#                 monkey_items[choices[i][0]].append(item)
#             else:
#                 monkey_items[choices[i][1]].append(item)
#             inspections[i] += 1

# chimps = sorted(inspections)
# print(chimps[-1] * chimps[-2])


for _ in range(10000):
    for i in range(len(tests)):
        while monkey_items[i]:
            item = monkey_items[i].pop(0)
            item = operation(i, item)
            item = item % common_mod
            if item % tests[i] == 0:
                monkey_items[choices[i][0]].append(item)
            else:
                monkey_items[choices[i][1]].append(item)
            inspections[i] += 1

chimps = sorted(inspections)
print(chimps[-1] * chimps[-2])
