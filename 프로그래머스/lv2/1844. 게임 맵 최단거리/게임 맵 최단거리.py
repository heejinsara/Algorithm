from collections import deque

def solution(maps):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    row=len(maps)
    col=len(maps[0])
    que=deque()
    que.append((0,0))
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<row and 0<=ny<col:
                if maps[nx][ny]==1:
                    maps[nx][ny]=maps[x][y]+1
                    que.append((nx,ny))
    if maps[-1][-1]!=1:
        return maps[-1][-1]
    else:
        return -1