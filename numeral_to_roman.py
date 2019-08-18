"""
function to convert numerical value to roman value.



"""


def main():
    n = int(input())
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
    print(result)

if __name__=="__main__":
    main()
