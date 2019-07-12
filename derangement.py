"""
In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position. In other words, a derangement is a permutation that has no fixed points.

a series is genrated like : for n = 0 to

1, 0, 1, 2, 9, 44, 265, 1854, 14833, 133496, 1334961, 14684570, 176214841, 2290792932

means n = 0
	1 derangement .
n=1 
	0 derangement
n =2
	1 derangement

n=3
	2 derangement

n = 4
	9 derangement

it is similar to fibonacci series with some modifications

Tn = (n-1)*((Tn-1)+(Tn-2))







"""

n = int(input())
a = 1
b = 0
while n >=2:
    a,b = b,(n-1)*(a+b)
    n-=1
print(b)



