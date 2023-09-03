from collections import deque

def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=1
    cnt=0
    while queue:
        v=queue.popleft()
        cnt+=1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=1
    return cnt
    

def solution(n, wires):
    answer=[]
    for i in range(len(wires)):
        temp=wires.copy()
        graph=[[] for _ in range(n+1)]
        visited=[0]*(n+1)
        temp.pop(i)

        for a,b in temp:
            graph[a].append(b)
            graph[b].append(a)

        for idx,g in enumerate(graph):
            if g!=[]:
                start=idx
                break

        cnt1=bfs(graph,start,visited)
        cnt2=n-cnt1
        answer.append(abs(cnt1-cnt2))
        
    return min(answer)