from collections import deque

def min_minutes_to_burn_forest(m, n, grid):
    queue = deque()
    total_trees = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))  
            if grid[i][j] == 1:
                total_trees += 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    minutes = 0
    burned_trees = 0

    while queue:
        x, y, minute = queue.popleft()
        minutes = max(minutes, minute) 
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                grid[nx][ny] = 2  
                queue.append((nx, ny, minute + 1))
                burned_trees += 1

    if burned_trees == total_trees:
        return minutes
    else:
        return -1

m, n = map(int, input().split()) 
grid = []

for i in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

result = min_minutes_to_burn_forest(m, n, grid)
print(result)
