def solution(triangle):
    for i in range(1,len(triangle)): #row
        for j in range(len(triangle[i])): #column
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j==len(triangle[i])-1:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j],triangle[i-1][j-1])
    return max(triangle[-1])