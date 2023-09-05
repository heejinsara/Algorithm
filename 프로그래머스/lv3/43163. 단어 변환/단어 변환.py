from collections import deque
def solution(begin, target, words):
    q=deque()
    q.append([begin,0]) #단어,깊이
    visited=[0]*len(words)
    while q:
        word,cnt=q.popleft()
        if word==target:
            return cnt
        for i in range(len(words)):
            temp=0
            if visited[i]==0:
                for j in range(len(begin)):
                    if word[j]!=words[i][j]:
                        temp+=1
            if temp==1:
                q.append([words[i],cnt+1])
                visited[i]=1
    return 0