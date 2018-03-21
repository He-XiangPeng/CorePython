import re

try:
    f = open('whodata.txt', 'r')
except IOError:
    print("no such file!")

for eachLine in f:
    print(re.split(r'\s\s+', eachLine))
f.close()
