'''
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(256)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
'''
import socket
socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#making a connection
socket1.connect(('data.pr4e.org',80))
command='GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
socket1.send(command)
while(True):
    dt=socket1.recv(8);#receive funciton is represented by recv-receive some lines
    if(len(dt)<1):
        break;
    print(dt.decode(),end='')
socket1.close()
