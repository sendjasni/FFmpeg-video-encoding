import socket
import sys

HOST = 'localhost'  # server name goes in here
PORT = 3820


def put(commandname):
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((HOST, PORT))

    socket1.send(commandname)

    string = 'ser.pdf'  # TODO : the name of file which i want to send

    # send file
    myfile = open(string).read()
    socket1.send(myfile)
    print 'PUT Successful'

    socket1.close()
    return


def get(commandname):
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((HOST, PORT))

    socket1.send(commandname)

    string = 'ser.pdf'  # TODO : the name of file which i want to receive

    with open(string, 'wb') as file_to_write:
        while True:
            data = socket1.recv(1024)
            # print data
            if not data:
                break
            # print data
            file_to_write.write(data)
    file_to_write.close()
    print 'GET Successful'
    socket1.close()
    return


msg = raw_input('Enter your name: ')
while True:
    print 'Instruction'
    print '"put " to send the file the server '
    print '"putInfo" to send the information to the server '
    print '"get" to receive the file from the server '
    print '"quit" to exit'

    sys.stdout.write('%s> ' % msg)
    inputCommand = sys.stdin.readline().strip()

    if inputCommand == 'quit':
        socket.send('quit')
        break

    elif inputCommand == 'put':
        put(inputCommand)

    elif inputCommand == 'putInfo':
        pass

    elif inputCommand == 'get':
        get(inputCommand)
