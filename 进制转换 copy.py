while True:
    a=input('请输入一个数字(输入Q结束程序):')
    if a.capitalize()=='Q':
       break
    else:
        c=int(a)
        print('十进制转->二进制:'+a+'->'+bin(c))
        print('十进制转->十六进制:'+a+'->%#x'%c)
        print('十进制转->八进制:'+a+'->%#o'%c)
    
