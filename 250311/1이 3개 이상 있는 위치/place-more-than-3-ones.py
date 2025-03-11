n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
result = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                cnt += 1
                if cnt >= 3: 
                    result += 1 
                    break

print(result)
