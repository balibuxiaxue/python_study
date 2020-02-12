def findstr():
    a=input('请输入目标字符串:')
    b=input('请输入子字符串（两个字符）：')
    a.count(b)
    print('子字符串在目标字符串中共出现', a.count(b) ,'次')
