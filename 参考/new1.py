lists=[1,2,3,4] #定义列表
number = range(1,5)
num=0
for i in number:
    a =lists[i-1]*1000 #取表里的数据拿来使用
    for m in number:
        if m == i:
            continue #打断循环,一般有两种方式,有break 和continue ,break 为结束循环,continue为结束本次循环继续下一次
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
    for b in num: #循环
        if b == a:
            continue
        for c in num:
            if c == a or c==b: #判断
                continue
            if a**3+b**3+c**3 == a*100+b*10+c:
                print("%d**3+%d**3+%d**3"%(a,b,c)) #输出类似C的printf("%d",&nun)

#递归

def fanXiang(name,n): 
    if len(name)==n:
        print("反向输出的名字是: ",end="")
        print(name[n-1],end="")
        return 0
    else:
        fanXiang(name,n+1)
        print(name[n-1],end="")
    if n==1:
        print("\n\n***反向完毕***")

#函数的调用
if __name__ == '__main__':
    name=input("输入你的名字:")
    fanXiang(name,1)


    
                
                