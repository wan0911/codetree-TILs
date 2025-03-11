# zip
# L = y행 이동만 보면 됨, dx = -1
# 각 양단 끝에 부딪히면, 방향 전환 dx => +1 / -1

N, T = map(int, input().split())
R, C, D = input().split()

x, y = int(R) - 1, int(C) - 1
dy = -1

while T > 0:
    T -= 1
    y = y + dy

    if y == 0 or y == N-1:
        T -= 1
        if dy == -1:
            dy = 1
        else:
            dy = -1


print(x + 1, y + 1)