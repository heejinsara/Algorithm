def solution(tickets):
    visited=[0]*len(tickets)
    answer = []
    def DFS(start, path):
        if len(path)==len(tickets)+1:
            answer.append(path)
            return
        for i, ticket in enumerate(tickets):
            if start==ticket[0] and visited[i]==0:
                visited[i]=1
                DFS(ticket[1],path+[ticket[1]])
                visited[i]=0
    DFS("ICN",["ICN"])
    answer.sort()
    return answer[0]