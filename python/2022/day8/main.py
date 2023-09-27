hm = [[int(x) for x in l.strip("\n")]for l in open("python/2022/day8/test.txt").readlines()]
hmt = list(map(list, zip(*hm)))

# Part 1
print((2 * len(hm)) + (2 * len(hm[0])) - 4 + len([0 for i in range(1, len(hm) - 1) for j in range(1, len(hm[i]) - 1) if (max(hm[i][0:j]) < hm[i][j] or max(hm[i][j + 1 : len(hm[i])]) < hm[i][j] or max(hmt[j][0:i]) < hm[i][j] or max(hmt[j][i + 1 : len(hm)]) < hm[i][j])]))

# Part 2
print((lambda p : max([p(list(reversed(hm[i][0:j])), hm[i][j]) * p(hm[i][j + 1 : len(hm[i])], hm[i][j]) * p(list(reversed(hmt[j][0:i])), hm[i][j]) * p(hmt[j][i + 1 : len(hm)], hm[i][j]) for i in range(1, len(hm) - 1) for j in range(1, len(hm[i]) - 1) ]))(lambda lst, curr : next((i for i, v in enumerate(lst) if v >= curr), len(lst)-1) + 1))
