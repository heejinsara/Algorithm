def solution(sizes):
    w=[]
    h=[]
    for i in sizes:
        temp=sorted(i, reverse=True)
        w.append(temp[0])
        h.append(temp[1])
    return max(w)*max(h)