print('同步测试')
print('''
爱因斯坦曾出过这样一道有趣的数学题：
      有一个长阶梯，若每步上2阶，最后剩1阶；
      若每步上3阶，最后剩2阶；
      若每步上5阶，最后剩4阶；
      若每步上6阶，最后剩5阶；
      只有每步上7阶，最后刚好一阶也不剩。
      ''')
temp=input('你想知道问题的答案吗？')
temp1=temp.upper()
if temp1=='YES' :
    a=100
    c=1
    while c==1:
        for i in range(a-100,a):
            if i%2==1 and i%3== 2 and i%5==4 and i%6==5 and i%7==0:
                print(i)
                c=2
                break
        else:
                a+=100
else:
    print('看来你并不想知道')
    temp2=input('请说出你的答案：')
    if int(temp2)==119 :
        print('正确')
    else:
              print('垃圾，答错了')
              
//测试2020 -1-添加ssh后 qiguai
//启动
        
 
   
