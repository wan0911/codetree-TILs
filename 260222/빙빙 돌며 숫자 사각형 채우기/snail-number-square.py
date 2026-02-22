n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 1. 달팽이(우->하->좌->상) 모양으로 돌면서 +1씩 증가
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
dir_num = 0

arr[x][y] = 1 # start

for i in range(2, n * m + 1):
    # next 방향 체크
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if (not in_range(nx, ny) or arr[nx][ny] != 0):
        dir_num = (dir_num + 1) % 4
    
    # 현재 x, y
    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i
  
# 2. 배열 출력
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()
