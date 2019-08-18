# Christmas tree program having input like
"""
input:

k = 3   (no of test cases)

next k line input n

n = 1
n = 3
n = 5
####
3
1
3
5
###

"""


k = int(input())
for i in range(k):
    n = int(input())
    if n<=1:
        print("You cannot generate christmas tree")
    elif n>20:
        print("Tree is no more")
    else:
        print(" "*n + "*")
        cor = 0
        for i in range(n,1,-1):
            temp = 3
            for j in range(i,0,-1):
                print(" "*(j-1+cor)+"*"*temp)
                temp+=2
            cor+=1
        print(" "*n + "*" )
        print(" "*n + "*" )
