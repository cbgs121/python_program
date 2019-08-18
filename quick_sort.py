def partition(A,p,r):
	key = A[r]
	i = p-1
	
	for j in range(p,r):   #loop will be executed only r-1 time
		
		if A[j]<= key:
			i=i+1
			A[i],A[j]=A[j],A[i]			# here swapping A[i] with A[j]
			
	A[i+1],A[r]=A[r],A[i+1]			# swapping A[i+1] and A[r]
		
	return i+1
	
def q_sort(A,p,r):
	if p<r:
		q = partition(A,p,r)
		q_sort(A,p,q-1)
		q_sort(A,q+1,r)
	return A

	
A = [4,3,1,5,6,5,7,7,32,22,2,12,21,8,9]
r = len(A)-1
p = 0 
print(q_sort(A,p,r))


