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
print('group1' + ' ' + re.match('(\w\w\w)-(\d\d\d)', 'abc-123').group(1))  # 注意子组()
print('group2' + ' ' + re.match('(\w\w\w)-(\d\d\d)', 'abc-123').group(2))  # 注意子组()
print(re.match('(\w\w\w)-(\d\d\d)', 'abc-123').groups())  # 全部子组
print(re.match('(a(b))', 'ab').groups())  # 两个子组

# 匹配字符串的起始和结尾以及单词边界，该操作符多用于搜索而不是匹配
print(re.search('^The', 'The end.').group())  # ^从起始处匹配
print(re.search('^The', 'end. The'))  # 不匹配
print(re.search(r'\bthe', 'bite the dog').group())  # 在边界
print(re.search(r'\bthe', 'bitethe dog'))  # 有边界
print(re.search(r'\Bthe', 'bitethe dog').group())  # 无边界


