import re
"""
正则表达式的使用

"""

m = re.match('foo', 'food on the table')
s = re.search('foo', 'seafood')
bt = 'bat|bet|bit'
mM = re.match(bt, 'bet')
mS = re.search(bt, "He bit me")
anyend = '.end'

if m is not None:
    print(m.group())

if s is not None:
    print(s.group())

if mM is not None:
    print(mM.group())

if mS is not None:
    print(mS.group())


print(re.match(bt, 'blt'))  # 不能匹配
print(re.match(bt, 'He bit me'))  # 不能匹配
print(re.match(anyend, 'bend').group())
print(re.match(anyend, 'end'))  # 不能匹配
print(re.match(anyend, '\nend'))  # 不能匹配\n-空格
print(re.search(anyend, 'The end').group())  # 用search匹配' '-空格
# print(m.group())
# print(s.group())
# print(mM.group())
