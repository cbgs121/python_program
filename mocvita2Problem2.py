
t = list(map(int,input().split(',')))

for i in range(12,0,-1):
    flg3 = 0
    flg2 = 0
    flg1 = 0
    a = i % 10
    b = i//10
    if (a in t) and (b in t):
        t.remove(a)
        t.remove(b)
        #flg3 = 0
        for j in range(31,0,-1):
            c = j%10
            d = j//10
            if (c in t) and (d in t):
                t.remove(c)
                t.remove(d)
                #flg2 = 0
                for k in range(23,-1,-1):
                    e = k%10
                    f = k//10
                    if (e in t) and (f in t):
                        t.remove(e)
                        t.remove(f)
                        #flg1 = 0
                        for l in range(59,-1,-1):
                            g = l%10
                            h = l//10
                            if (g in t) and (h in t):
                                t.remove(g)
                                t.remove(h)
                                #print("{b}{a}/{d}{c} {f}{e}:{h}{g}".format(b,a,d,c,f,e,h,g))
                                print("{}{}/{}{} {}{}:{}{}".format(b,a,d,c,f,e,h,g))
                                flg1 = 1
                                break
                        if flg1 == 1:
                            flg2 = 1
                            break
                if flg2 == 1:
                    flg3 = 1
                    break
        if flg3 == 1:
            break

if flg1 != 1:
    print(0)
