def solution(name):
    min_move=len(name)-1
    answer=0
    for idx, char in enumerate(name):
        answer+=min(ord(char)-ord('A'),ord('Z')-ord(char)+1)
        next=idx+1
        while next<len(name) and name[next]=='A':
            next+=1
        min_move=min(min_move,2*(idx)+len(name)-next, idx+2*(len(name)-next))
    answer+=min_move
    return answer