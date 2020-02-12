a=input('请输入需要检查的密码组合：')
b=len(a)
c=0
d=0
e=0
list_4=[]
m=list(a)
for M in m:
    if M!='p':
        list_4.append(M)
list_1=r'~!@#$%^&*()_=-/,.?<>;:[]{}|\p'
list_2='abcdefghijklmnopqresuvwxyz'
list_3='1234567890'
if b <= 8 :
    print ('您的密码安全评级评定为：低')
    print('''# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位''')
else:
    for each in a.casefold():
        if each in list_1:
            c+=1
        if each in list_2:
            d+=1
        if each in list_3:
            e+=1
f_index=e+d+e
if a[0] in list_2 and c>=3 and b!=0 and b>=16 and f_index>=3:
    print('您的密码安全评定等级为：高')
    f_index=0
if f_index>=2 and b>=8:
    print('您的密码安全评定等级为：中')
    print(r'''# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位''')  


        
