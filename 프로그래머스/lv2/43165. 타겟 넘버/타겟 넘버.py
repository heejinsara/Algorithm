'''
def solution(numbers, target):
    leaves=[0]
    for num in numbers:
        temp=[]
        for leaf in leaves:
            temp.append(leaf-num)
            temp.append(leaf+num)
        leaves=temp
    answer=leaves.count(target)
    return answer
'''
cnt=0
def DFS(numbers, target, idx, value):
    global cnt
    if idx==len(numbers) and value==target:
        cnt+=1
        return
    elif idx==len(numbers):
        return
    DFS(numbers, target, idx+1, value+numbers[idx])
    DFS(numbers, target, idx+1, value-numbers[idx])

def solution(numbers, target):
    global cnt
    DFS(numbers, target, 0, 0)
    return cnt