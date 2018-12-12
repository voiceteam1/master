  # -*- coding:utf-8 -*- 
l1 = [[1,1,1],[2,2,2],[3,3,3]]
for i in l1:
    print (i)
num = 0
for i in range(3):
	for j in range(3):
		a=l1[i]
		b =a[j]
		if i==j:
			num+=b
print ('对角线之和为%d'%num)
