def countfu(x):
    list_1= r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
    L=len(list_1)-2
    a=[1]
    s=0
    while s<=L:
        a=a.append(0)
        s+=1   
    i=0
    I=0
    b=len(x)-1
    while i<=b:
        while I<=L:
            if x[i]==list_1[I]:
                a[I]+=1
            I+=1
        i+=1
    print(list_1)
    print(a)
x=input('请输入检测的数据')
countfu(x)
