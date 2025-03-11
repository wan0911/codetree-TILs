# zip
# L = y행 이동만 보면 됨, dx = -1
# 각 양단 끝에 부딪히면, 방향 전환 dx => +1 / -1

# 상하좌우, x/y 모든 경우에 대해 만들어야 함

N, T = map(int, input().split())
R, C, D = input().split()
x, y = int(R) - 1, int(C) - 1
mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

move_dir = mapper[D]
dk = 1 if move_dir == 0 or 2 else -1
while T > 0:
    T -= 1
    if move_dir == 0 or move_dir == 3:
        y = y + dk
        if y == 0 or y == N-1:
            T -= 1
            if dk == -1:
                dk = 1
            else:
                dk = -1
    else:
        x = x + dk
        if x == 0 or x == N-1:
            T -= 1
            if dk == -1:
                dk = 1
            else:
                dk = -1

print(x + 1, y + 1)