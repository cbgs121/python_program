single_digits = ["", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

two_digits = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens_multiple = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

tens_power = ["hundred", "thousand", "ten thousand"]


def fun(num):
    if len(num)==1:
        return single_digits[ord(num)-48+1]
    num = num.lstrip('0')
    if len(num)==0:
        return ''
    if len(num)==1:
        return single_digits[ord(num)-48+1]
    elif len(num)==2:
        if int(num) in range(10, 20):
            return two_digits[int(num) % 10]
        else:
            if num[-1] == '0' and int(num[0]) >= 2:
                return tens_multiple[int(num[0])]
            else:
                return tens_multiple[int(num[0])]+" " + single_digits[int(num[-1])+1]
    elif len(num) == 3:
        return single_digits[int(num[0])+1]+" " + tens_power[0]+" " + fun(num[1:])
    elif len(num) == 4:
        return single_digits[int(num[0]) + 1]+" " + tens_power[1]+" " + fun(num[1:])
    elif len(num) == 5:
        return fun(num[:2])+" " + 'thousand' + " " + fun(num[2:])

def main():
    m, n = map(int,input().split())
    a = fun(str(m))
    flag = 0
    b = fun(str(n))
    if m==n:
        print(m,end='')
    else:
        while (a < b and m < n) or (a > b and m > n):
            m = m*2
            n = n*2
            if m>99999 or n>99999 or m+n > 99999:
                print("Out of bounds",end='')
                flag = 1
                break
            else:
                a = fun(str(m))
                b = fun(str(n))
        if flag != 1 and m+n < 99999:
            print(m+n,end='')


if __name__ == '__main__':
    main()

