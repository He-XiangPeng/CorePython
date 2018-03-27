from socket import *

'''
Python3 TCP 时间戳客户端
'''

HOST = '127.0.0.1'  # or 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

try:
    while True:
        data = input('> ')
        if data == 'offline':
            break
        tcpCliSock.sendall(bytes(data, 'utf-8'))
        data = str(tcpCliSock.recv(BUFSIZ), 'utf-8')
        print(data)
except ConnectionResetError:
    tcpCliSock.close()
