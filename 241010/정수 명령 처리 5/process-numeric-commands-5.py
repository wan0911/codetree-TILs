from sys import stdin


N = int(stdin.readline().rstrip())
arr = []

for _ in range(N):
    command = stdin.readline().rstrip().split(' ')
    s = command[0]
    
    if s == 'push_back':
        arr.append(int(command[1]))
    elif s == 'pop_back':
        arr.pop()
    elif s == 'size':
        print(len(arr))
    elif s == 'get':
        print(arr[int(command[1]) - 1])