# Part 1
def adjacent(head, tail):
    return (
        False
        if tail
        not in [
            (head[0] + a[0], head[1] + a[1])
            for a in [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)]
        ]
        else True
    )


head = (0, 0)
tail = (0, 0)
visited = {(0, 0)}
for l in open("python/2022/day9/test.txt").readlines():
    direction, length = l.split()
    length = int(length)
    for i in range(length):
        offset = 1 if direction in "RU" else -1
        if direction in "LR":
            head = (head[0] + offset, head[1])
        else:
            head = (head[0], head[1] + offset)
        if adjacent(head, tail):
            pass
        else:
            lr_offset = 1 if (head[0] - tail[0]) > 0 else -1
            ud_offset = 1 if (head[1] - tail[1]) > 0 else -1
            lr_offset = 0 if (head[0] - tail[0]) == 0 else lr_offset
            ud_offset = 0 if (head[1] - tail[1]) == 0 else ud_offset
            tail = (tail[0] + lr_offset, tail[1] + ud_offset)
            visited.add(tail)

print(len(visited))

# Part 2

visited = {(0, 0)}
rope = [(0, 0) for _ in range(10)]


def move_tail(index):
    head = rope[index]
    tail = rope[index + 1]
    if adjacent(head, tail):
        pass
    else:
        lr_offset = 1 if (head[0] - tail[0]) > 0 else -1
        ud_offset = 1 if (head[1] - tail[1]) > 0 else -1
        lr_offset = 0 if (head[0] - tail[0]) == 0 else lr_offset
        ud_offset = 0 if (head[1] - tail[1]) == 0 else ud_offset
        tail = (tail[0] + lr_offset, tail[1] + ud_offset)
    rope[index + 1] = tail
    if index >= len(rope) - 2:
        return tail
    return move_tail(index + 1)


for l in open("python/2022/day9/test.txt").readlines():
    direction, length = l.split()
    length = int(length)
    offset = 1 if direction in "RU" else -1
    for i in range(length):
        head = rope[0]
        if direction in "RL":
            rope[0] = (head[0] + offset, head[1])
        else:
            rope[0] = (head[0], head[1] + offset)
        tail = move_tail(0)
        visited.add(tail)

print(len(visited))
