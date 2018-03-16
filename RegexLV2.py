import re
"""

正则表达式的LV2级应用

"""
# ?匹配0次或者1次
patt = '\w+@(\w+\.)?\w+\.com'
print(re.match(patt, 'nobody@xxx.com').group())
print(re.match(patt, 'nobody@www.xxx.com').group())
print(re.match(patt, 'nobody@www.xxx.yyy.zzz.com'))  # 不能匹配

# *匹配0次或者多次
patt2 = '\w+@(\w+\.)*\w+\.com'
print(re.match(patt2, 'nobody@www.xxx.yyy.zzz.com').group())

# 特殊字符
print(re.match('\w\w\w-\d\d\d', 'abc-123').group())
print(re.match('\w\w\w-\d\d\d', 'abc-xyz'))  # 不能匹配

# 分组
print('group ' + re.match('(\w\w\w)-(\d\d\d)', 'abc-123').group(0))  # 完整匹配
print('group1' + ' ' + re.match('(\w\w\w)-(\d\d\d)',
                                'abc-123').group(1))  # 注意子组()
print('group2' + ' ' + re.match('(\w\w\w)-(\d\d\d)',
                                'abc-123').group(2))  # 注意子组()
print(re.match('(\w\w\w)-(\d\d\d)', 'abc-123').groups())  # 全部子组
print(re.match('(a(b))', 'ab').groups())  # 两个子组

# 匹配字符串的起始和结尾以及单词边界，该操作符多用于搜索而不是匹配
print(re.search('^The', 'The end.').group())  # ^从起始处匹配
print(re.search('^The', 'end. The'))  # 不匹配
print(re.search(r'\bthe', 'bite the dog').group())  # 在边界
print(re.search(r'\bthe', 'bitethe dog'))  # 有边界
print(re.search(r'\Bthe', 'bitethe dog').group())  # 无边界

# 使用findall()和finditer()查找每一次出现的位置
list1 = re.findall('car', 'car')
print(list1)
list2 = re.findall('car', 'scary')
print(list2)
list3 = re.findall('car', 'carry the barcardi to the car')
print('list3[1]: ' + list3[1])

s = 'This and that.'
list4 = re.findall(r'(th\w+) and (th\w+)', s, re.I)
print(type(list4))
for item in list4:
    print(item)
# python3.6.4无法编译，2.7.10可编译
# print(re.finditer(r'(th\w+) and (th\w+)', s, re.I).next().groups())
for m in re.finditer(r'(th\w+) and (th\w+)', s, re.I):
    print(m)

# 使用sub()和subn()搜索和替换
print(re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X, \n'))
print(re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X, \n'))
print(re.sub('[ae]', 'X', 'abcedf'))
print(re.subn('[ae]', 'X', 'abcedf'))

print(re.split(':', 'str1:str2:str3'))
DATA = ('Moutain View, CA 94040', 'Sunnyvale, CA', 'Los Altos, 94023',
        'Cupertino, 95014', 'Palo Alto CA')
for datum in DATA:
    print(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum))

print(re.findall(r'(?i)yes', 'yes? Yes. YES!!'))  # 使用re.I/IGNORECASE
# 使用re.I/IGNORECASE
print(re.findall(r'(?i)th\w+', 'The quickest way is through this tunnel.'))
# 使用re.M/MULTILINE
print(re.findall(r'(?im)(^th[\w ]+)', '''
This line is the first,
another line,
that line, it's the best
    '''))  # 新一行前不能有tab，空格等字符

# re.S/DOTAALL, 该标记表示点号(.)能够用来表示\n符号(反之其通常用于表示除了\n之外的全部字符)
print(re.findall(r'th.+', '''
    This first line,
    the second line,
    the third line
    '''))
print(re.findall(r'(?s)th.+', '''
    This first line,
    the second line,
    the third line
    '''))


