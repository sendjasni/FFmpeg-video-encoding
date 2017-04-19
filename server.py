import socket
import sys

HOST = 'localhost'
PORT = 3820

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))

socket.listen(1)
while True:
    conn, addr = socket.accept()
    print 'New client connected ..'

    string = 's.pdf'  # TODO : the name of file which i want to send

    reqCommand = conn.recv(1024)
    print 'Client> %s' % (reqCommand)

    if reqCommand == 'quit':
        break

    elif reqCommand == 'put':

        with open(str(addr)+'-'+string, 'wb') as file_to_write:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                # print data
                file_to_write.write(data)

        file_to_write.close()
        print 'Receive Successful'

    elif reqCommand == 'get':
        myfile = open(string).read()
        conn.send(myfile)
        print 'Send Successful'

    conn.close()

socket.close()
