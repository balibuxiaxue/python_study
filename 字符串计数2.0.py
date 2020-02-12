def countstr(a,c):
    i=0
    b=len(a)
    sum=0

    while (i+1) <=(b-1):
        if a[i]==c[0] and a[i+1]==c[1]:
            sum+=1
        i+=1
    print('计数结果是',sum)
    
a=input('请输入你要检索的字符串：')
c=input('请输入你要计数的字符串：')
countstr(a,c)
