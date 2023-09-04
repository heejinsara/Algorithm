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