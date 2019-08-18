t = int(input())
for _ in range(t):
    n = int(input())
    mt = []
    for i in range(n):
        mt.append(input())
    flag = 0
    flg = 0
    for i in range(n):
        for j in range(n // 2):
            if mt[i][j] != mt[i][n - 1 - j]:
                flag = 1
                break
        if flag ==1:
            break
    for i in range(n):
        for j in range(n // 2):
            if mt[j][i] != mt[n - 1 - j][i]:
                flg = 1
                break
        if flg == 1:
            break

    if flag != 1 and flg != 1:
        print("YES")
    else:
        print("NO")