n = int(input("Enter No\n"))
lp = [0]*(n+1)
pr = []
for i in range(2,n+1):
    if lp[i]==0:
        lp[i]=i
        pr.append(i)
    j = 0
    while j <(len(pr)) and pr[j]<=lp[i] and i*pr[j]<=n:
	lp[i*pr[j]]=pr[j]
	j+=1
print(pr)
print(len(pr))

"""
def sieve_linear(n):
    prime = [0]*(n+1)
    pr = []
    for i in range(2,n+1):
        if prime[i]==0:
            prime[i]=i
            pr.append(i)
        j = 0
        while j<len(pr) and pr[j]<=prime[i] and i*pr[j]<=n:
            prime[i*pr[j]] = pr[j]
            j+=1
    print(pr)

sieve_linear(1000000)

"""
