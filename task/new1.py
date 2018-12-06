lists=[1,2,3,4]
number = range(1,5)
num=0
for i in number:
	a =lists[i-1]*1000
	for m in number:
		if m == i:
			continue
		b = lists[m-1]*100
		for n in number:
			if n ==i or n==m:
				continue
			c = lists[n-1]*10
			x = 10-(i+n+m)
			d = a+b+c+lists[x-1]
			print("不相同的数字有：%d"%d)
			num +=1
print("总的个数有%d"%num)
#水仙花
print("*"*20)
num =range(1,10)
for a in num:
	for b in num:
		if b == a:
			continue
		for c in num:
		    if c == a or c==b:
		        continue
			if a**3+b**3+c**3 == a*100+b*10+c:
			    print("%d**3+%d**3+%d**3"%(a,b,c))


				
					