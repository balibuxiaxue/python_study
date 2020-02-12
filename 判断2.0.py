string=input('判断是否是回文联：')
def fun_1(string):
    a1=len(string)
    a=a1//2
    b=0
    i=0
    for i in range(a):
        if string[i]==string[a1-i-1]:
            b+=1
        i+=1
    if b==a:
        print('是回文联')
    else:
        print('不是回文联')

fun_1(string)
        
