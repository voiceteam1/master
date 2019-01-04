M=0
N=0

for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            N=100*i+10*j+k
            if (i**3+j**3+k**3==N):
                M+=1
                print (i,j,k)
print("所有的水仙花数为:",M)
        
