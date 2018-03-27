from socket import *
from time import ctime

'''
Python3 TCP 时间戳服务器

'''

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

try:
    while True:
        print('waiting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('...connected from:', addr)

        while True:
            data = str(tcpCliSock.recv(BUFSIZ), 'utf-8')
            if data == 'offline':
                break
            tcpCliSock.sendall(bytes(ctime(), 'utf-8') + bytes('\n', 'utf-8') +
                               bytes(data, 'utf-8'))

        tcpCliSock.close()
except OSError:
    tcpSerSock.close()
