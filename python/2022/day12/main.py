grid = [list(x) for x in open("python/2022/day12/test.txt").read().split("\n")]
start = (0, 0)
starts = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i, j)
            starts.append((i, j))
        elif grid[i][j] == "a":
            starts.append((i, j))


def calculate_shortest_path(grid: list, start: tuple):
    visited = {start}
    queue = [start]
    steps = {start: 0}
    while queue:
        curr = queue.pop(0)
        curr_symbol = "a" if curr == start else grid[curr[0]][curr[1]]
        curr_ord = ord(curr_symbol)
        if curr_symbol == "E":
            return steps[curr]
        neighbours = [
            (curr[0] - 1, curr[1]),
            (curr[0] + 1, curr[1]),
            (curr[0], curr[1] + 1),
            (curr[0], curr[1] - 1),
        ]
        for neighbour in neighbours:
            if (
                -1 in neighbour
                or neighbour[0] >= len(grid)
                or neighbour[1] >= len(grid[0])
            ):
                continue
            neighbour_symbol = grid[neighbour[0]][neighbour[1]]
            neighbour_symbol = "z" if neighbour_symbol == "E" else neighbour_symbol
            neighbour_ord = ord(neighbour_symbol)
            if (
                (neighbour_ord - 1 == curr_ord) or (neighbour_ord <= curr_ord)
            ) and neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                steps[neighbour] = steps[curr] + 1
    return 0


print(calculate_shortest_path(grid, start))
print(min(filter(lambda x: x != 0, [calculate_shortest_path(grid, x) for x in starts])))
