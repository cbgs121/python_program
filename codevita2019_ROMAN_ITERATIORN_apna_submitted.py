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

n = int(input())
while n>=1 and n<=3999:
    st = roman(n)
    mx = max(list(st))
    if ord(mx) >= 48 and ord(mx)<=57:
        base = ord(mx)-48+1
    else:
        base = ord(mx)-ord('A')+10+1
    k = 0
    temp = 0 
    for i in st[::-1]:
        if ord(i)>=48 and ord(i)<=57:
            bs = ord(i)-48
        else:
            bs = ord(i)-ord('A')+10
        temp += bs*(base**k)
        k+=1
    n = temp
   
print(n)
