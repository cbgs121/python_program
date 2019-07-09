

lt = list(input().split(' '))
serch = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', \
'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ans = []
for i in lt:
    t = []
    for j in i:
        t.append(serch.index(j)+1)
    mx = max(t)
    #print(mx)
    sm  = 0
    d = len(i)
    #print("i = {},d = {}".format(i,d))
    while(d>0):
        #print(serch.index(i[d-1]),mx**(d-1))
        sm+=serch.index(i[-d+1])*mx**(d-1)
        d-=1
    ans.append(sm)
print(min(ans))
