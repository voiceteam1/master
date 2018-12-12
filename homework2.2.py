# -*- coding: utf-8 -*-
 #运用列表生成器输出杨辉三角形
def triangles():
    N=[1]
    while True:
        yield N        #generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
        N.append(0)    #了解yeild用法
        N=[N[i-1] + N[i] for i in range(len(N))]  #写法
if __name__ == '__main__':
	n=0
	for t in triangles():
		print(t)
		n=n+1
		if n == 10:
			break
	



#格式化输出杨辉三角形
def triangle(num):
    triangle=[[1]]
    for i in range(2,num+1):
        triangle.append([1]*i)
        for j in range(1,i-1):
            triangle[i-1][j]=triangle[i-2][j]+triangle[i-2][j-1]
    return triangle
def printtriangle(triangle,width):
    column=len(triangle[-1])*width
    for sublist in triangle:
        result=[]
        for contents in sublist:
            result.append('{0:^{1}}'.format(str(contents),width))#控制各行数字间距
        print('{0:^{1}}'.format(''.join(result),column))#控制缩进
        
if __name__=='__main__':
    num=int(input('num:'))
    triangle=triangle(num)
    width=len(str(triangle[-1][len(triangle[-1])//2]))+3
    printtriangle(triangle,width)

