from itertools import permutations

def isprime(number):
    if number<=1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True

def solution(numbers):
    answer=[]
    for i in range(len(numbers)):
        for k in permutations(numbers,i+1):
            temp=int(''.join(k))
            if isprime(temp):
                answer.append(temp)
    return len(set(answer))