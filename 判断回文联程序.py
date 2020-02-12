def funtion_1(a):
    i=0
    b=len(a)//2
    c=len(a)-1
    s=0
    while   i<b:
        if a[i]==a[c-i]:
            print(a[i])
            s+=1
        i+=1
    if s!=b:
        print('不是回文联！')
        print(s)
    else:
        print('是回文联！')
        print(s)
        
a=input('请输入一句话：')
funtion_1(a)

    
