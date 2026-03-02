N = int(input())

# 1. stack 클래스 생성
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        return 1 if (not self.items) == True else 0
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items[-1]

# 2. 스택 함수 실행
# push만 출력 X
s = Stack()
for _ in range(N):
    line = input().split()
    command = line[0]

    if command == "push":
        val = line[1]
        s.push(val)
    elif command == "pop":
        print(s.pop())
    elif command == "size":
        print(s.size())
    elif command == "empty":
        print(s.empty())
    elif command == "top":
        print(s.top())



