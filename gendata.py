from random import randrange, choice
from string import ascii_lowercase as lc
from math import pow
# from sys import maxsize
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    dtint = randrange(pow(2, 32) - 1)    # pick date
    # dtint = 2 ** 32 - 1  # 另一种2的32次幂的表示法
    # dtint = randrange(maxsize)    # 64位操作系统数字为long int 2**64 -1
    dtstr = ctime(dtint)          # date string
    llen = randrange(4, 8)          # login is shorter
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)      # domain is longer
    dom = ''.join(choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d' %
          (dtstr, login, dom, choice(tlds), dtint, llen, dlen))
