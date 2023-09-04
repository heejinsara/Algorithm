def solution(n, computers):
    answer = 0
    visited=[0]*n
    for com in range(n):
        if visited[com]==0:
            DFS(n, computers, com, visited)
            answer+=1
    return answer

def DFS(n, computers, com, visited):
    visited[com]=1
    for connect in range(n):
        if com!=connect and computers[com][connect]==1:
            if visited[connect]==0:
                DFS(n, computers, connect, visited)