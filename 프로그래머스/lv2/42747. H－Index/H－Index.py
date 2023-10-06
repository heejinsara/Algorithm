# import numpy as np
# def solution(citations):
#     citations.sort(reverse=True)
#     for i in citations:
#         temp=len(np.where(np.array(citations)>=i))
#         print(temp)
#         if temp>=i & len(citations)-temp<=i:
#             return i
def solution(citations):
    citations.sort(reverse=True)
    #print(citations)
    for i in range(len(citations)):
        if i+1>citations[i]:
            return i
    return len(citations)