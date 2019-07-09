"""                                       Question

            Television Sets
Problem Description

Dr. Vishnu is opening a new world class hospital in a small town designed to be the first preference of the
patients in the city. Hospital has N rooms of two types - with TV and without TV, with daily rates of R1 and
R2 respectively.
However, from his experience Dr. Vishnu knows that the number of patients is not constant throughout the
year, instead it follows a pattern. The number of patients on any given day of the year is given by the following
formula –
(6-M)^2 + |D-15| where
M is the number of month (1 for jan, 2 for feb ...12 for dec) and
D is the date (1,2...31).
All patients prefer without TV rooms as they are cheaper, but will opt for with TV rooms only if without
TV rooms are not available. Hospital has a revenue target for the first year of operation. Given this target and
the values of N, R1 and R2 you need to identify the number of TVs the hospital should buy so that it meets the
revenue target. Assume the Hospital opens on 1st Jan and year is a non-leap year

Constraints
Hospital opens on 1st Jan in an ordinary year
5 <= Number of rooms <= 100
500 <= Room Rates <= 5000
0 <= Target revenue < 90000000
Input Format
First line provides an integer N that denotes the number of rooms in the hospital
Second line provides two space-delimited integers that denote the rates of rooms with TV (R1) and without TV
(R2) respectively
Third line provides the revenue target
Output
Minimum number of TVs the hospital needs to buy to meet its revenue target. If it cannot achieve its target,
print the total number of rooms in the hospital.
Test Case
ExplanationExample 1
Input
20
1500 1000
7000000
Output
14
Explanation
Using the formula, number of patients on 1st Jan will be 39, on 2nd Jan will be 38 and so on. Considering
there are only twenty rooms and rates of both type of rooms are 1500 and 1000 respectively, we will need 14
TV sets to get revenue of 7119500. With 13 TV sets Total revenue will be less than 7000000
Example 2
Input
10
1000 1500
10000000
Output
10
Explanation
In the above example, the target will not be achieved, even by equipping all the rooms with TV. Hence, the
answer is 10 i.e. total number of rooms in the hospital.

"""


n = int(input())
m = list(map(int, input().split(' ')))
rtv_c = max(m)
r_c = min(m)
revnue = int(input())


def fun(n, rtv, r, rtv_c, r_c):
    total = 0
    cost = 0
    for i in range(1, 13):
        mnt = (6 - i) ** 2
        if i == 2:
            for j in range(1, 29):
                t = mnt + abs(15 - j)
                if t >= n:
                    total += 20
                    cost += (r * r_c + rtv_c * rtv)
                else:
                    total += t
                    if t >= r:
                        cost += (r * r_c + (t - r) * rtv_c)
                    else:
                        cost += (t * r_c)

        elif i == 4 or i == 6 or i == 9 or i == 11:
            for j in range(1, 31):
                t = mnt + abs(15 - j)
                if t >= n:
                    total += 20
                    cost += (r * r_c + rtv_c * rtv)
                else:
                    total += t
                    if t >= r:
                        cost += (r * r_c + (t - r) * rtv_c)
                    else:
                        cost += (t * r_c)
        else:
            for j in range(1, 32):
                t = mnt + abs(15 - j)
                if t >= n:
                    total += 20
                    cost += (r * r_c + rtv_c * rtv)
                else:
                    total += t
                    if t >= r:
                        cost += (r * r_c + (t - r) * rtv_c)
                    else:
                        cost += (t * r_c)
    return cost


flag = 0
for rtv in range(n):
    if fun(n, rtv, n - rtv, rtv_c, r_c) >= revnue:
        flag = 1
        break
    # print(rtv,fun(n,rtv,n-rtv,rtv_c,r_c))

if flag == 1:
    print(rtv)
else:
    print(n)
