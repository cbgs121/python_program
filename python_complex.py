"""
To sort a given sting on the basis of another string 

"""

s = 'zyxwvutsrqponmlkjihgfedcba'
t = 'abcde'
print(''.join(sorted(t,key=s.index)))


#   End

