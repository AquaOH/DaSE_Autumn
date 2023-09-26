import re
p = '^[0-9]{17}[0-9XY]$'
s1 = input("请输入身份证号: ")
if re.match(p,s1) == None:
    print("无效身份证")
else:
    print("有效身份证")
