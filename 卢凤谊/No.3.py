score=input("请输入成绩:")

score=int(score)
if (score>=90 and score<=100):
    print ("成绩等级",'A')
if (score<90 and score>=60):
    print ("成绩等级",'B')
if (score<60 and score>=0):
    print ("成绩等级",'C')

