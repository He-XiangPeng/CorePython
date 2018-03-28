from socket import *
# from time import ctime

'''
Python3 UDP 时间戳服务器

'''

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

try:
    while True:
        print('waiting for message...')
        data, addr = udpSerSock.recvfrom(BUFSIZ)  # 接收的数据报是bytes类型
        print(': '.join(['received message', str(data, 'utf-8')]))
        if data == bytes('offline', 'utf-8'):
            print('one client is offline!')
            # break
            # 根据不同的情况关闭服务器端
        print('...received from and returned to:', addr)

except OSError:
    udpSerSock.close()
