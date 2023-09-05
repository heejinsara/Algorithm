def dfs(n, computers, com1, visited):
    visited[com1]=1
    for com2 in range(n):
        if com1!=com2 and computers[com1][com2]==1 and visited[com2]==0:
            dfs(n, computers, com2, visited)
            
    

def solution(n, computers):
    visited=[0]*n
    answer=0
    for com1 in range(n):
        if visited[com1]==0:
            dfs(n, computers, com1, visited)
            answer+=1
    return answer