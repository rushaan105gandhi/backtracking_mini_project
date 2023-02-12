import random
import timeit


def d(matrix):
    print()
    for ITEM in matrix:
        print(*ITEM)
    print()


def getPath(i, j):
    if i == j == 0:
        return

    x, y = visited[i][j][0]
    sample_paths.append([i, j])
    getPath(x, y)


rows = int(input("\nEnter number of rows: "))
columns = int(input("Enter number of columns: "))

mat = [[random.randint(0, 1) for _ in range(columns)] for _ in range(rows)]

mat[0][0] = 1

d(mat)

visited = [[[] for _ in range(columns)] for _ in range(rows)]

q = [[0, 0]]

paths = 0

start = timeit.default_timer()

while len(q) > 0:
    pt = q.pop(0)
    x, y = pt

    # the top left corner
    if pt == [0, 0]:
        if mat[x][y + 1] != 0:
            q.append([x, y + 1])
            visited[x][y + 1].append([0, 0])

        if mat[x + 1][y + 1] != 0:
            q.append([x + 1, y + 1])
            visited[x + 1][y + 1].append([0, 0])

        if mat[x + 1][y] != 0:
            q.append([x + 1, y])
            visited[x + 1][y].append([0, 0])


    elif y == columns - 1:
        if mat[x][y] == 1:
            paths += 1


    elif rows - 1 > x > 0 == y:
        for i in range(x - 1, x + 2):
            for j in range(y, y + 2):
                if (i != x or j != y) and mat[i][j] != 0 and ([i, j] not in visited[x][y]):
                    q.append([i, j])
                    visited[i][j].append([x, y])

    # bottom left corner
    elif x == rows - 1 and y == 0:
        if mat[x][y + 1] != 0 and ([x, y + 1] not in visited[x][y]):
            q.append([x, y + 1])
            visited[x][y + 1].append([x, y])

        if mat[x - 1][y + 1] != 0 and ([x - 1, y + 1] not in visited[x][y]):
            q.append([x - 1, y + 1])
            visited[x - 1][y + 1].append([x, y])

        if mat[x - 1][y] != 0 and ([x - 1, y] not in visited[x][y]):
            q.append([x - 1, y])
            visited[x - 1][y].append([x, y])


    elif x == 0:
        for i in range(x, x + 2):
            for j in range(y - 1, y + 2):
                if (i != x or j != y) and mat[i][j] != 0 and ([i, j] not in visited[x][y]):
                    q.append([i, j])
                    visited[i][j].append([x, y])


    elif x == rows - 1:
        for i in range(x - 1, x + 1):
            for j in range(y - 1, y + 2):
                if (i != x or j != y) and mat[i][j] != 0 and ([i, j] not in visited[x][y]):
                    q.append([i, j])
                    visited[i][j].append([x, y])

    elif 0 < x < rows - 1 and 0 < y < columns - 1:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i != x or j != y) and mat[i][j] != 0 and ([i, j] not in visited[x][y]):
                    q.append([i, j])
                    visited[i][j].append([x, y])

    else:
        print(pt, "Error")
        break

stop = timeit.default_timer()

all_paths = []

for i in range(rows):
    if len(visited[i][columns - 1]) > 0:
        sample_paths = []
        getPath(i, columns - 1)
        sample_paths.append([0, 0])
        sample_paths.reverse()
        all_paths.append(sample_paths)

if paths > 0:
    print("Some of the possible paths are: \n")

    for item in all_paths:
        print()
        print(*item, sep=' -> ')
        print("Cost of the path is:", len(item) - 1)

print("\nTotal number of paths:", paths)

print("\nTime taken:", stop - start, "seconds")
