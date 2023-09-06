from heapq import *
def solution(operations):
    result=[]
    for operation in operations:
        if operation[0]=='I':
            result.append(int(operation.split()[-1]))
        elif len(result)>0:
            if operation=='D -1':
                result.remove(min(result))
            elif operation=='D 1':
                result.remove(max(result))
    if len(result)==0:
        return [0,0]
    else:
        return [max(result),min(result)]