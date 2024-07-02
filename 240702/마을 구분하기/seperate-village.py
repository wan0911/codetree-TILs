import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def dfs(x, y, cnt):
    visited[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
            cnt = dfs(nx, ny, cnt + 1)

    return cnt

res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            res.append(dfs(i, j, 1))

res.sort()
print(len(res))
print(*res, sep = '\n')