"""
codevita alternative solution 


"""


def roman(n):
    nm = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    rmn = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    result = ''
    i = 12
    while n>0:
        j = n//nm[i]
        n = n%nm[i]
        while j>0:
            result+=rmn[i]
            j-=1
        i-=1
    return result

# print(roman(901))

search = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',\
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',\
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

n = int(input())
# print("Some middle calculation")
while n>=1 and n<=3999:
    st = roman(n)
    mx = max(list(st))
    base = search.index(mx)+1
    k = 0
    temp = 0 
    for i in st[::-1]:
        temp += search.index(i)*(base**k)
        k+=1
    n = temp
    # print("roman value : ",st,"----->value in base {} : ".format(base), n)
    
print(n)
