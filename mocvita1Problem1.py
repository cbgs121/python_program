# moc vita problem 1
def sub(st, n, rs):
    su = []
    for Len in range(1, n + 1):
        for i in range(n - Len + 1):
            j = i + Len - 1
            ss = ''
            for k in range(i, j + 1):
                ss += st[k]
            if len(ss) == len(rs):
                su.append(ss)
    return su


def main():
    s=list()
    s.append(input())
    s.append(input())
    for i in range(int(s[1])):
        p,q=map(str,input().split())
        s.append(p)
        s.append(q)
    st=s[0]
    rs=''
    for i in range(2,2*int(s[1])+1,2):
        if s[i]=="L":
            st=st[int(s[1+i]):]+st[:int(s[1+i])]
            rs+=st[0]
        elif s[i]=="R":
            st=st[len(st)-int(s[i+1]):]+st[:len(st)-int(s[i+1])]
            rs+=st[0]
    ss=sub(s[0],len(st),rs)
    tt=0
    for i in ss:
        flag=0
        for j in i:
            if i.count(j)!=rs.count(j):
                flag=1
                break
        if flag==0:
            tt=1
            break

    if tt==1:
        print("YES")
    else:
        print("NO")


if __name__=='__main__':
    main()