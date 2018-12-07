M=0
for i in range(1,5):
    for j in range(1,5):
        
        for k in range(1,5):
            if i!=j and i!=k and j!=k:
                M+=1
                print(i,j,k,end="     ")     
print("能组成互不相同且无重复的三位数的个数为:",M)
                    
