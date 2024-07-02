import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    cnt = 1

    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt                 

res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            res.append(bfs(i, j))

res.sort()
print(len(res))
print(*res, sep = '\n')