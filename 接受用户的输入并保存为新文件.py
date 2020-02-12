file_name=input('请输入文件名：')
file_name=file_name+'.txt'
print(  '''请输入内容【单独输入':w'保存退出】：''')
f=open(file_name,'w')
stop_word=':w'
str1=''
for line in iter(input,stop_word):
    str1 += line+'\n'
f.write(str1)
f.close()
