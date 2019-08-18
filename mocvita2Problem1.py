import math


def f(n):
    if n < 0:
        return math.inf
    if n == 0:
        return 1
    else:
        return n * f(n - 1)


# all combination without constraint

def funall(x, s, y, m, z, c):
    rst = (f(x) / (f(x - s) * f(s))) * (f(y) / (f(y - m) * f(m))) * (f(z) / (f(z - c) * f(c)))
    print(int(rst))


# combination for both in same group

def func(x, s, y, m, z, c):
    rst = 2 * (f(x - 2) / (f(x - s - 1) * f(s - 1))) * (f(y) / (f(m) * f(m - y))) * (f(z) / (f(c) * f(z - c))) + 1
    print(int(rst))


# combination for different group
def func2(x, s, y, m, z, c):
    rst1 = (f(x - 1) / (f(x - 1 - s) * f(s))) * (f(y - 1) / (f(y - m) * f(m - 1))) * (f(z) / (f(z - c) * f(c)))
    rst2 = (f(x - 1) / (f(s - 1) * f(x - s))) * (f(y - 1) / (f(m) * f(y - m - 1))) * (f(z) / (f(c) * f(z - c)))
    rst = rst1 + rst2 + 1
    print(int(rst))


x = int(input())

s = int(input())

y = int(input())

m = int(input())

z = int(input())

c = int(input())

p, q = map(str, input().split(" "))

r = input()

t = ord(r) - ord('A')

funall(x, s, y, m, z, c)

# for element use once
#print(t)
if t in range(x):
    x = x - 1
elif t in range(x, x + y):
    y = y - 1
elif t in range(x + y, x + z + y + 1):
    z = z - 1
# print(x,s,y,m,z,c)
flg1 = ord(p) - ord('A')
flg2 = ord(q) - ord('A')

if flg1 > t and flg2 > t:
    flg1 -= 1
    flg2 -= 1
elif flg1 < t and flg2 > t:
    flg2 -= 1
if flg1 > t and flg2 < t:
    flg1 -= 1

if flg1 in range(x) and flg2 in range(x):
    func(x, s, y, m, z, c)
if flg1 in range(x, y + x) and flg2 in range(x, x + y):
    func(y, m, x, s, z, c)
if flg1 in range(x + y, x + y + z) and flg2 in range(x + y, x + y + z):
    func(z, c, x, s, y, m)
if flg1 in range(x) and flg2 in range(x, y + x):
    func2(x, s, y, m, z, c)
if flg1 in range(x) and flg2 in range(y + x, z + x + y):
    func2(x, s, z, c, y, m)
if flg1 in range(x, y + x) and flg2 in range(x + y, z + x + y):
    func2(y, m, z, c, x, s)


"""
# Input
3
2
3
2
3
2
A C
D
Output
27
7
"""