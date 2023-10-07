from itertools import permutations
def isprime(N):
    if N<=1:
        return False
    for i in range(2,int(N**0.5)+1):
        if N%i==0:
            return False
    return True

def solution(numbers):
    result=[]
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            temp=int(''.join(j))
            if isprime(temp):
                result.append(temp)
    return len(set(result))