from collections import deque
def solution(begin, target, words):
    answer = 0
    que=deque()
    que.append([begin,0]) #단어, 깊이
    visited=[0]*len(words)
    while que:
        word,cnt=que.popleft()
        if word==target:
            answer=cnt
            break
        for i in range(len(words)):
            temp_cnt=0
            if visited[i]==0:
                for j in range(len(word)):
                    if word[j]!=words[i][j]:
                        temp_cnt+=1
                if temp_cnt==1:
                    que.append([words[i],cnt+1])
                    visited[i]=1
                
    return answer