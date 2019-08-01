"""
1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17, …

This series is a mixture of 2 series – all the odd terms in this series form a Fibonacci series and all the even terms are the prime numbers in ascending order. 

Write a program to find the Nth term in this series. 

The value N is a Positive integer that should be read from STDIN. The Nth term that is calculated by the program should be written to STDOUT. Other than the value of Nth term, no other characters/strings or message should be written to STDOUT. 







"""


def fib(k):
    i = 1
    j = 1
    while k>2:
        j,i = i+j,j
        k-=1
    print(j)
    


def prime(k):
    lt = []
    j = 2
    while k>0:
        flag = 0
        for i in lt:
            if j%i==0:
                flag = 1
                break
        if flag != 1:
            lt.append(j)
            k-=1
        j+=1
    print(lt[-1])
    
# /prime(25)
n = int(input())

if n&1 == 1:
    k = n//2 + 1
    fib(k)
else:
    k = n//2
    prime(k)
        
