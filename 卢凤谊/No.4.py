string=input("请输入你的名字:")
for i in range(0,len(string)):
    print(string[len(string)-i-1],end='')#这里加end干甚?
print(zaigai)