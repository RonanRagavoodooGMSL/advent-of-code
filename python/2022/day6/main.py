word = open("python/2022/day6/test.txt").readline()
for i in range(len(word) - 3):
    if len(set(word[i : i + 4])) == 4:
        print(i + 4)
        break
