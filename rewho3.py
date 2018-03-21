import os
import re

# io(Python 3) 对象的上下文管理器会自动调用f.close()
with os.popen("who", "r") as f:
    for eachLine in f:
        print(re.split(r'\s\s+|\t', eachLine.strip()))
