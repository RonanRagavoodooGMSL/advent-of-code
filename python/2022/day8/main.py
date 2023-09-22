height_matrix = [
   [int(x) for x in line.strip("\n")] for line in open("python/2022/day8/test.txt").readlines()
]
vis_matrix = [[1 if (x==0 or x==len(height_matrix[0]) - 1 or y==0 or y==len(height_matrix) - 1) else 0 for x in range(0, len(height_matrix[0]))] for y in range(0, len(height_matrix))]

count = (2 * len(height_matrix)) + (2 * len(height_matrix[0])) - 4

for i in range(1, len(vis_matrix) - 1):
    for j in range(1, len(vis_matrix[i]) - 1):
        if (vis_matrix[i][j - 1] in (1,2)) and (height_matrix[i][j-1] < height_matrix[i][j]):
            vis_matrix[i][j] = 1
            count += 1
        elif (vis_matrix[i-1][j] in (1,2)) and (height_matrix[i-1][j] < height_matrix[i][j]):
            vis_matrix[i][j] = 1
            count += 1
        elif (vis_matrix[i][j - 1] in (1,2)) and (height_matrix[i][j-1] == height_matrix[i][j]):
            vis_matrix[i][j] = 2
        elif (vis_matrix[i-1][j] in (1,2)) and (height_matrix[i-1][j] == height_matrix[i][j]):
            vis_matrix[i][j] = 2


for i in range(len(vis_matrix) - 2, 0, -1):
    for j in range(len(vis_matrix[i]) - 2, 0, -1):
            if (vis_matrix[i][j] == 1):
                pass
            elif (vis_matrix[i][j+1] in (1,2)) and (height_matrix[i][j+1] < height_matrix[i][j]):
                vis_matrix[i][j] = 1
                count += 1
            elif (vis_matrix[i+1][j] in (1,2)) and (height_matrix[i+1][j] < height_matrix[i][j]):
                vis_matrix[i][j] = 1
                count += 1
            elif (vis_matrix[i][j+1] in (1,2)) and (height_matrix[i][j+1] == height_matrix[i][j]):
                vis_matrix[i][j] = 2
            elif (vis_matrix[i+1][j] in (1,2)) and (height_matrix[i+1][j] == height_matrix[i][j]):
                vis_matrix[i][j] = 2

# for x in vis_matrix:
#     print(" ".join([str(a) for a in x]))
print(count)