"""
Mine codevita 2019 Salary problem2

"""

slab = list(map(int, input().split()))
tax = list(map(int, input().split()))
rebate = int(input())
lt = list(map(int, input().split()))
temp = [0]
for i in range(len(slab)-1):
    temp.append((slab[i+1]-slab[i])*tax[i]//100)

newtemp = []
sm = 0
for i in temp:
    sm += i
    newtemp.append(sm)
total = 0
for i in lt:
    for j in range(len(newtemp)):
        if i <= newtemp[j]:
            break
        elif j >= len(slab)-1:
            j += 1
    k = i - newtemp[j-1]
    x = (k * 100) // tax[j-1]
    total += slab[j-1]+x

print(total+len(lt)*rebate)


"""
test case 1:

300000 600000 900000
10 20 30
100000
90000 150000 210000 300000

Output:

5300000

Test case 2:

400000 500000 600000
10 20 30
100000
1000000 2000000 3000000

Output:
21799999


"""
