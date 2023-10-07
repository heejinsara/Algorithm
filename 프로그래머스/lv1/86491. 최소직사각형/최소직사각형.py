def solution(sizes):
    L1=[]
    L2=[]
    for i in sizes:
        L1.append(max(i))
        L2.append(min(i))
    return max(L1)*max(L2)