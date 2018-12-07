a = [1,2,3,4]
count = 0
for i in a:
	for j in a:
		for k in a: 
			if(i!=j!=k):#这个表达有问题
				A =100*i+10*j+k
				count +=1
				print(A)

print('次数=',format(count))

