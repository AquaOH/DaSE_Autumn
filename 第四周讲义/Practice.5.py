# 正则表达式——限定符
import re

# Ca + bC 表示b之前a至少出现一次
# Ca * bC 表示b之前a出现0次或多次
# Ca ? bC 表示b之前a出现0次或1次
# a与b均表示单个字符

p1 = 'rei+sen'
p2 = 'rei*sen'
p3 = 'rei?sen'

str1 = "reisen"
str2 = "reiisen"
str3 = "resen"
print(re.match(p1, str1), re.match(p1, str2), re.match(p1, str3))
print(re.match(p2, str1), re.match(p2, str2), re.match(p2, str3))
print(re.match(p3, str1), re.match(p3, str2), re.match(p3, str3))

# {n} n为自然数 匹配确定的n次
# {n,} n为自然数,匹配至少n次 o{0,}等价限定符*,o{1,}等价限定符+
# {n,m} n,m为自然数,n<=m,匹配n<=Amount<=m,o{0,1}等价o?

# 正则表达式——普通字符
# [ABC] 匹配中括号内字符
# [^ABC] 匹配除了中括号内字符
# [A-Z] 表示区间,匹配所有大写字母 [a-z]表示所有小写字母 [0-9]表示所有数字
# . 匹配除换行符(\n \r)之外任何单个字符,等价[^\n\r]
# [\s\S]匹配所有 其中\s匹配所有空白符,包括换行(\n \r)，\S匹配非空白符,不包括换行
# \w 匹配字母、数字、下划线,等价[A-Za-z0-9_]
print("\n************************分割线*****************************\n")



# 正则表达式——贪婪匹配与非贪婪匹配
# + * 限定符都是贪婪匹配,他们会匹配尽可能多的文字
# 如果想变为非贪婪匹配,需要在它们后面加? 如+？ *？,修改为最小匹配模式
# 示例文本:<h1>RUNOOB-菜鸟教程</h1>
# 贪婪:/<.*>/ 匹配结果<h1>RUNOOB-菜鸟教程</h1>
# 非贪婪/最小匹配:/<.*?>/ 匹配结果<h1>
# 通过在 *、+ 或 ? 限定符之后放置 ?，该表达式从"贪婪"表达式转换为"非贪婪"表达式或者最小匹配。


# 正则表达式——定位符
# ^ 匹配字符串开始的位置.注意与中括号内表示式用法分开,如^Chapter [1-9][0-9]?
# $ 匹配字符串结尾的位置
# \b 匹配一个单词边界,即字与空格的位置
# \B 匹配非单词边界,如\Bapt,表示apt在单词中间