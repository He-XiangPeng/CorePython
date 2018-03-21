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

# re.X/VERBOSE&(?:...)
print(re.search(r'''(?x)
            \((\d{3})\) # 区号
            [ ]         # 空白符
            (\d{3})     # 前缀
            -           # 横线
            (\d{4})     # 终点数字
    ''', '(800) 555-1212').groups())
print(re.findall(r'http://(?:\w+\.)*(\w+\.com)',
                 'http://google.com http://www.google.com http://code.google.com'))
print(re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',
                '(800) 555-1212').groupdict())
print(re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',
             '(\g<areacode>) \g<prefix>-xxxx', '(800) 555-1212'))

# (?x)匹配电话号码
print(bool(re.match(r'''(?x)

        # match (800) 555-1212, save areacode, prefix, no.
        \((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})

        # space
        [ ]

        # match 800-555-1212
        (?P=areacode)-(?P=prefix)-(?P=number)

        # space
        [ ]

        # match 18005551212
        1(?P=areacode)(?P=prefix)(?P=number)


    ''', '(800) 555-1212 800-555-1212 18005551212')))

# (?=...)&(?!...)
print(re.findall(r'\w+(?= van Rossum)',
                 '''
                    Guido van Rossum
                    Tim Peters
                    Alex Martelli
                    Just van Rossum
                    Raymond Hettinger
    '''))
print(re.findall(r'(?m)^\s+(?!noreply|postmaster)(\w+)',
                 '''
                sales@phptr.com
                postmaster@phptr.com
                eng@phptr.com
                noreply@phptr.com
                admin@phptr.com
    '''))
print(['%s@aw.com' % e.group(1) for e in
       re.finditer(r'(?m)^\s+(?!noreply|postmaster)(\w+)',
                   '''
        sales@phptr.com
        postmaster@phptr.com
        eng@phptr.com
        noreply@phptr.com
        admin@phptr.com
        ''')
       ])

# 只匹配xy即x后紧跟y
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy')))
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xx')))

# 使用Python原始字符串
# print(re.match('\bblow', 'blow').group())  # \bblow不匹配
print(re.match('\\bblow', 'blow').group())  # \\bblow匹配
print(re.match(r'\bblow', 'blow').group())  # 使用raw string

# gendata.py练习
data = 'Wed Dec 23 19:42:46 2099::lcgg@zgaufnf.org::4101709366-4-7'
Gen_patt = '^(Tue|Wed|Thu|Fri|Sat|Sun)'
Gen_M = re.match(Gen_patt, data)
print(Gen_M.group())
print(Gen_M.group(1))
print(Gen_M.groups())

# 更国际化的表达
Gen_patt_IN = '^(\w{3})'
print(re.match(Gen_patt_IN, data).group())

# 搜索与匹配......还有贪婪
print(re.search(r'\d+-\d+-\d+', data).group())  # 目的匹配\d-\d-\d，匹配失败
print(re.match(r'.+\d+-\d+-\d+', data).group())  # .+ 贪婪的操作符
# 输出Wed Dec 23 19:42:46 2099::lcgg@zgaufnf.org::4101709366-4-7
print(re.match(r'.+(\d+-\d+-\d+)', data).group(1))  # .+ 贪婪的操作符,使用圆括号分组
print(re.match(r'.+?(\d+-\d+-\d+)', data).groups())  # .+ ？非贪婪的操作符
# 输出('4101709366-4-7',)
