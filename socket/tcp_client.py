

from socket import *

class TcpClient:

    HOST='127.0.0.1'

    PORT=1122

    BUFSIZE=1024

    ADDR=(HOST,PORT)

    def __init__(self):
        self.client=socket(AF_INET,SOCK_STREAM)
        self.client.connect(self.ADDR)

        while True:

            data=input('input:')
            if not data:
                break


            self.client.send(data.encode('utf8'))

            print('send%s:%s'%(self.HOST,data))

            if data.upper()=="QUIT":
                break

            data=self.client.recv(self.BUFSIZE)

            if not data:
                break

            print('from%s:%s'%(self.HOST,data.decode('utf8')))

if __name__ == '__main__':
    client=TcpClient()
