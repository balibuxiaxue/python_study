string=input('请输入需要判断的字符串：')
def fun1(string):
    a=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    b=(0,1,2,3,4,5,6,7,8,9)
    c=(' ')
    a1=0
    b1=0
    c1=0
    i=0
    lenth=len(string)
    while i<lenth:
        if string[i] in a:
            a1+=1
        if string[i] in b:
            b1+=1
        if string[i] in c:
            c1+=1
        i+=1
    d1=lenth-a1-b1-c1
    print(a1,b1,c1,d1)

fun1(string)

