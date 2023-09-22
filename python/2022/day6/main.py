# Part 1
print((lambda x :[i for i in range(4, len(x)) if len(set(x[i - 4 : i])) == 4][0])(open("python/2022/day6/test.txt").readline()))
# Part 2
print((lambda x :[i for i in range(14, len(x)) if len(set(x[i - 14 : i])) == 14][0])(open("python/2022/day6/test.txt").readline()))
