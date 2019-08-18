"""
To import sum function of other file in current file 
"""
'''
from file_name import function_name
	# Note : File name should be without extension
	#now we can use function_name as it is the from same file

import file_name

# Now if we have to use the function then we have to use file_name.function_name()

'''

#End


"""
To sort a given sting on the basis of another string 

"""
import math
s = 'zyxwvutsrqponmlkjihgfedcba'
t = 'abcde'
print(''.join(sorted(t,key=s.index)))


#   End
def is_leap_year():
	year = int(input())
	if (year%4==0 and year%100!=0) or (year%4==0 and year%100==0 and year%400==0):
		print("Yes")
	else:
		print('No')

is_leap_year()

#  End

# todo sum of factorial of digit of no is equal to no then no is strong 
def is_strong():
	n = int(input())
	test = n
	sm = 0
	while n>0:
		k = n%10
		n//=10
		sm+=math.factorial(k)
	if sm==test:
		print("Yes")
	else:
		print("No")

is_strong()




#	End

def is_armstrong():
	n = int(input())
	k = n
	digit = 0
	while n>0:
		digit+=1
		n//=10
	sm = 0	
	n = k
	while n>0:
		d = n%10
		n//=10

		sm += d**digit 
	if k == sm:
		print("Yes")
	else:
		print("No")

is_armstrong()

#	End

# Sum of all factor of number is equal to no

def is_perfect_no():
	n = int(input())
	i=2
	test = n
	sm = 1
	while i*i<n:
		if n%i==0:
			sm+=i+n//i
		i+=1
	if test == sm:
		print("Yes")
	else:
		print("No")


is_perfect_no()


#	End
