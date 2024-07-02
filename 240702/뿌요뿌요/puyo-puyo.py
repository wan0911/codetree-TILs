# 1 ~ 100
# 블럭: 같은 숫자, 블럭 개수 >= 4 -> 터짐
# 터지게 되는 블럭 수, 최대 블럭 크기 (터지는거 상관 X)

import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

def dfs(x, y, num, cnt):
    visited[x][y] = 1

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == num and not visited[nx][ny]:
            cnt = dfs(nx, ny, num, cnt + 1)
    return cnt

bomb_cnt, max_len = 0, 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            check = dfs(i, j, graph[i][j], 1)

            if check >= 4:
                bomb_cnt += 1

            if max_len < check:
                max_len = check

print(bomb_cnt, max_len)