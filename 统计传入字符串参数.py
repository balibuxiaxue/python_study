def funtion_1(*a):
    b='abcdefghijklmnopqrstuvwxyz'
    c='0123456789'
    d=0
    e=0
    f=0
    i=0
    while i <=(len(*a)-1):
        for each in a[i]:
            if each.casefold() in b:
                d+=1
            if each in c:
                e+=1
            else:
                f+=1
        print('第',i,'个字符串共有字母',d,'个,数字',e,'个')
        i+=1
