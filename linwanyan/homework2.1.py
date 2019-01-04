a = input("请输入一个数：")
b = int(a)

def sum(n):#求和
	if n%2==0:
		f = sum1(n)
		print(f)
	else:
		f = sum2(n)
		print(f)
def sum1(n):#偶数求和
	s = 0
	a = 1
	while (a<=(n//2)):
		s = s+1/(2*a)
		a +=1
	return(s)
def sum2(n):#奇数求和
	s,a = 0,0
	while (a<=(n-1)//2):
		s = s+1/(2*a+1)
		a += 1
	return (s)

def main(n):
	sum(n)

main(b)





