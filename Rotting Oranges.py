from collections import deque

def orangesRotting(grid):
    rows = len(grid)

    if rows == 0:
        return -1

    cols = len(grid[0])

    rotten = deque()
    count_fresh = 0
    count_minutes = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                rotten.append((row, col))
            elif grid[row][col] == 1:
                count_fresh += 1
    
    while rotten and count_fresh > 0:
        count_minutes += 1

        for _ in range(len(rotten)):
            x, y = rotten.popleft()

            for x2, y2 in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                xx, yy = x + x2, y + y2

                if xx < 0 or xx == rows or yy < 0 or yy == cols:
                    continue

                if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                    continue

                count_fresh -= 1
                grid[xx][yy] = 2
                rotten.append((xx, yy))

    return count_minutes if count_fresh == 0 else -1
            
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))