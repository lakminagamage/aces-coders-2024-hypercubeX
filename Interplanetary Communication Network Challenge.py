# n, m = map(int, input().split())
n,m = 5 ,3

cost_matrix = [[2,5,1],[3,4,7],[8,1,2],[6,2,4],[3,8,8]]

# for i in range(n):
#     cost_matrix.append([int(x) for x in input().strip().split()])

print(cost_matrix)
connected_mars = [False] * m
connected_earth = [False] * n

total_cost = 0 

min_cost = {}
for i in range(len(cost_matrix)):
    min_value = min(cost_matrix[i])
    for j in range(m):
        if cost_matrix[i][j] == min_value:
            min_cost[(i, j)] = min_value


print(min_cost)

