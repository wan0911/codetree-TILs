# 올바른 괄호 -> 스택
# 왼 -> 오 순으로 읽기
line = input()

def chk_line(str):
    stack = []

    for i in range(len(str)):
        word = str[i]

        if word == '(':
            stack.append(word)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
        
    if len(stack) != 0:
        return False
    return True

if chk_line(line) == True:
    print('Yes')
else:
    print('No')

