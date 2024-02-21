import sys
N, K = map(int, sys.stdin.readline().split())
HISTORY, ANS = None, 0
for _ in range(N):
    X = int(sys.stdin.readline())
    if HISTORY == None: HISTORY = X
    else:
        if HISTORY>=X+K:ANS+=1
    HISTORY = X
print(ANS)
