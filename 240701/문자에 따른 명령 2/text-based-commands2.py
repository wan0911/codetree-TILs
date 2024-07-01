# rotation 개념

import sys

input = sys.stdin.readline
 
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 3
x, y = 0, 0

tmp = list(input().rstrip())
for t in tmp:
    if t == 'L':
        dir_num = (dir_num + 3) % 4 # 시계 방향
    if t == 'R':
        dir_num = (dir_num + 1) % 4
    if t == 'F':
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)