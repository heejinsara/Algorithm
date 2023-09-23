def solution(numbers):
    result=sorted(list(map(str,numbers)),key=lambda x:(x*4)[:4],reverse=True)
    answer=str(int(''.join(result)))
    return answer