def solution(array, commands):
    answer=[]
    for command in commands:
        i=command[0]
        j=command[1]
        k=command[2]
        new_array=sorted(array[i-1:j])
        answer.append(new_array[k-1])
    return answer