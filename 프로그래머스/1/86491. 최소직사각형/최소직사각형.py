def solution(sizes):
    L1=[]
    L2=[]
    for s in sizes:
        L1.append(min(s))
        L2.append(max(s))
    return max(L1)*max(L2)