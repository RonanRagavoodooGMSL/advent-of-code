tree = {}
curr_dir = []
res = 0
sizes = []


def recurse(path):
    global res
    total = sum([int(x) if x.isnumeric() else recurse(f"{path}/{x}") for x in tree[path]])
    res += total < 100000 and total
    return total


def recurse2(path):
    sizes.append(total := sum([int(x) if x.isnumeric() else recurse2(f"{path}/{x}") for x in tree[path]]))
    return total


for line in [x.strip("\n").split(" ") for x in open("python/2022/day7/test.txt").readlines() if not x.startswith("$ ls")]:
    if "".join(line).startswith("$cd"):
        curr_dir.pop() if line[2] == ".." else curr_dir.append(line[2])
    else:
        if "/".join(curr_dir) in tree:
            tree["/".join(curr_dir)].append(line[1] if line[0] == "dir" else line[0])
        else:
            tree["/".join(curr_dir)] = [line[1] if line[0] == "dir" else line[0]]
        

recurse("/")
print(res)
free_space = recurse2("/") - 40000000
print(min(list(filter(lambda x: (x > free_space), sizes))))
