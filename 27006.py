def kmp(pattern, text):
    N = len(pattern)
    pi = [0] * N
    j = 0
    for i in range(1, N):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    starts = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == N:
                starts.append(i - N + 1)
                j = pi[j - 1]
    return starts

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    Grid = []
    for i in range(N):
        Grid.append(input())
    possible = [True] * N
    for k in range(N):
        diagonal = []
        for i in range(N):
            j = (k - i) % N
            diagonal.append(Grid[i][j])
        S = ''.join(diagonal)
        R = S[0] + S[:0:-1]
        text = R + R[:-1]
        good = [False] * N
        starts = kmp(S, text)
        for p in starts:
            c = (-p) % N
            D = (c - k) % N
            good[D] = True
        for D in range(N):
            if not good[D]:
                possible[D] = False
        if not any(possible):
            break
    answer = sum(possible) * N
    print(answer)