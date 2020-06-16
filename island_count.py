def island_count(adj):
    count = 0    
    visited = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and adj[i][j] == 1:
                dfs(adj, i, j, visited)
                count += 1
    return count

def dfs(adj, x, y, visited):
    visited[x][y] = 1
    delta_x = [-1, -1, -1, 0, 1, 1, 1, 0]
    delta_y = [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(8):
        if issafe(x + delta_x[i], y + delta_y[i], n):
            if visited[x + delta_x[i]][y + delta_y[i]] == 0:
                if adj[x + delta_x[i]][y + delta_y[i]] == 1:
                    dfs(adj, x + delta_x[i], y + delta_y[i], visited)

def issafe(x, y, n):
    if x >= 0 and x < n and y >= 0 and y < n:
        return True
    return False


n = int(input("Enter matrix size: "))
adj = []
for i in range(n):
    adj.append(list(map(int, input().split())))
print("No. of Islands: ", island_count(adj))
