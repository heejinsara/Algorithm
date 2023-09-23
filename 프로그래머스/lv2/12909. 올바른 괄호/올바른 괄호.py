from collections import deque
def solution(s):
    s=deque(s)
    if s[0]==')':
        return False
    result=0
    while s:
        temp=s.popleft()
        if temp=='(':
            result+=1
        else:
            result-=1
        if result<0:
            return False
    if result==0:
        return True
    else:
        return False