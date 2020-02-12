i=3
while i!=0:
        temp=input('请输入密码:  ')
        if temp =='wangdasha' :
                print('密码正确，进入程序.....')
                break
        else:
                if  '*' in temp:
                        print('密码中不能含有“*”号！你还有',i,'次机会!',end=' ')
                else:
                        i-=1
                        print('密码输入错误！你还有',i,'次机会!',end=' ')

