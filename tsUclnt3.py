from socket import *

'''
Python3 UCP 时间戳客户端
'''

HOST = '127.0.0.1'  # or 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

try:
    while True:
        data = input('> ')
        udpCliSock.sendto(data.encode('utf-8'), ADDR)
        if data == 'offline':
            break
except ConnectionResetError:
    udpCliSock.close()
