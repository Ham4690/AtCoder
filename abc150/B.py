def checkABC(S):
    count = 0
    for i in range(len(S)):
        if S[i] == 'A':
            if i+1 < len(S) and S[i+1] == 'B':
                if i+2 < len(S) and S[i+2] == 'C':
                    count += 1
    
    return count


N = int(input())

S = list(input())

print(checkABC(S))