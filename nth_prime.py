def main(k):
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

if __name__=='__main__':
	main(int(input()))
