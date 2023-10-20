def solution(s):
    result=[]
    for i in s:
        try:
            if i=='(':
                result.append('(')
            else:
                result.pop()
        except:
            return False
    return len(result)==0