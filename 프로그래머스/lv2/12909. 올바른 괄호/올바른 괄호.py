from collections import deque
def solution(s):
    s=deque(s)
    temp=[s.popleft()]
    if temp[0]==')':
        return False
    for i in s:
        try:
            if i=='(':
                temp.append('(')
            elif i==')':
                temp.pop()
        except:
            return False
    if len(temp)==0:
        return True
    else:
        return False