n = int(input())
count = 3*(n-1)
a = 6
b = 28
d = 16
for i in range(1,n+1):
    print(" "*count,end='')
    for j in range(i):
        print("{:05d}".format(a),end=" ")
        a,b = b,b+(b-a)+d
    count-=3
    print()
