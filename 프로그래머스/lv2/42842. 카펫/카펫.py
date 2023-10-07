def solution(brown, yellow):
    for i in range(1,yellow+1):
        if yellow%i==0:
            if 4+2*(i+yellow//i)==brown:
                return [yellow//i+2,i+2]