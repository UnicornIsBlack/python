

import socket

port=8081

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('',port))

print('wait...')

while True:
    data,addr=s.recvfrom(1024)
    print('received:',data,'from',addr)

    
