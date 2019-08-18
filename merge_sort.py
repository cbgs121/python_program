import math
def merge_fun(A,p,q,r):
	n1 = q-p+1
	n2 = r-q
	left = [0]*(n1)
	right = [0]*(n2)
	
	for i in range(n1):
		left[i] = A[p+i]
	left.append(math.inf)
	
	for j in range(n2):
		right[j] = A[q+j+1]
	right.append(math.inf)
	
	i,j = 0,0
	
	for k in range(p,r+1):
		if left[i]>right[j]:
			A[k] = right[j]
			j+=1
		else:
			A[k]=left[i]
			i+=1


def merge_sort(A,p,r):
	if p<r:
		q = (p+r)//2
		merge_sort(A,p,q)
		merge_sort(A,q+1,r)
		merge_fun(A,p,q,r)
		
	return A


