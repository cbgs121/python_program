"""
                                        Question 2
Prime Fibonnaci
Problem Description
Given two numbers n1 and n2
1. Find prime numbers between n1 and n2, then
2. Make all possible unique combinations of numbers from the prime numbers list you found in step 1.
3. From this new list, again find all prime numbers.
4. Find smallest (a) and largest (b) number from the 2nd generated list, also count of this list.
5. Consider smallest and largest number as the 1st and 2nd number to generate Fibonacci series respectively
till the count (number of primes in the 2nd list).
6. Print the last number of a Fibonacci series as an output
Constraints
2 <= n1, n2 <= 100
n2 - n1 >= 35
Input Format
One line containing two space separated integers n1 and n2.
Output
Last number of a generated Fibonacci series.
Test Case
Explanation
Example 1
    Input
        2 40
    Output
        13158006689
Explanation1st prime list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
Combination of all the primes = [23, 25, 27, 211, 213, 217, 219, 223, 229, 231, 237, 32, 35, 37, 311, 313, 317,
319, 323, 329, 331, 337, 52, 53, 57, 511, 513, 517, 519, 523, 529, 531, 537, 72, 73, 75, 711, 713, 717, 719,
723, 729, 731, 737, 112, 113, 115, 117, 1113, 1117, 1119, 1123, 1129, 1131, 1137, 132, 133, 135, 137, 1311,
1317, 1319, 1323, 1329, 1331, 1337, 172, 173, 175, 177, 1711, 1713, 1719, 1723, 1729, 1731, 1737, 192, 193,
195, 197, 1911, 1913, 1917, 1923, 1929, 1931, 1937, 232, 233, 235, 237, 2311, 2313, 2317, 2319, 2329, 2331,
2337, 292, 293, 295, 297, 2911, 2913, 2917, 2919, 2923, 2931, 2937, 312, 315, 317, 3111, 3113, 3117, 3119,
3123, 3129, 3137, 372, 373, 375, 377, 3711, 3713, 3717, 3719, 3723, 3729, 3731]
2nd prime list=[193, 3137, 197, 2311, 3719, 73, 137, 331, 523, 1931, 719, 337, 211, 23, 1117, 223, 1123, 229,
37, 293, 2917, 1319, 1129, 233, 173, 3119, 113, 53, 373, 311, 313, 1913, 1723, 317]
smallest (a) = 23
largest (b) = 3719
Therefore, the last number of a Fibonacci series i.e. 34th Fibonacci number in the series that has 23 and 3719
as the first 2 numbers is 13158006689
Example 2
    Input
        30 70
    Output
        2027041
Explanation
1st prime list=[31, 37, 41, 43, 47, 53, 59, 61, 67]
2nd prime list generated form combination of 1st prime list = [3137, 5953, 5347, 6761, 3761, 4337, 6737,
6131, 3767, 4759, 4153, 3167, 4159, 6143]
smallest
prime
largest prime in 2nd list=6761
in
2nd
list=3137
Therefore, the last number of a Fibonacci series i.e. 14th Fibonacci number in the series that has 3137 and
6761 as the first 2 numbers is 2027041


"""
import math

n1, n2 = map(int, input().split(' '))
# n1,n2 = 30,70
lt = []
# prime no between n1 and n2
for i in range(max(n1, 2), n2):
    flag = 0
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            flag = 1
            break
    if flag != 1:
        lt.append(i)
# prime no between n1 and n1 store in list lt


# no formed by concatenating digit of prime no obtained above

temp = []


def dig(n):
    sm = 0
    while n > 0:
        sm += 1
        n //= 10
    return sm


for i in range(len(lt)):
    for j in range(len(lt)):
        if i != j:
            temp.append(lt[i] * 10 ** dig(lt[j]) + lt[j])


# print(len(temp))

# new list is formed temp and value is store in temp


# to find no which is prime in temp

def primetolast(n1, n2):
    ptl = []

    for i in range(max(2, n1), n2 + 1):
        flag = 0
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                flag = 1
                break
        if flag != 1 and i in temp:
            ptl.append(i)

    return (ptl)


# list plt return from above function having all prime no out of list temp


x = primetolast(temp[0], temp[-1])


# print(x)
# print(x[0],x[-1])

# to print last no of fibonacci series having first and last of list x as first two no of series

def fibb(n, a, b):
    while n != 2:
        a, b = b, a + b
        n -= 1
    print(b, end=' ')


fibb(len(x), x[0], x[-1])