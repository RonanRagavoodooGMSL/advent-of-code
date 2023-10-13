import string

# Part 1
print(sum([{k: v for (k, v) in list(zip(list(string.ascii_lowercase + string.ascii_uppercase),[p for p in range(1, 53)]))}[x] for x in [list(set([x for x in pair[0] if x in pair[1]]))[0] for pair in [(c[:int(len(c) / 2)], c[int(len(c) / 2):]) for c in [l.strip() for l in open("python/2022/day3/test.txt").readlines()]]]]))

# Part 2
print((lambda r : (sum([[{k: v for (k, v) in list(zip(list(string.ascii_lowercase + string.ascii_uppercase),[p for p in range(1, 53)]))}[i] for i in g[0] if i in g[1] and i in g[2]][0] for g in [r[i : i + 3] for i in range(0, len(r), 3)]])))([set(x.strip()) for x in open("python/2022/day3/test.txt").readlines()]))
