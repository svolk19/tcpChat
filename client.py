import socket

def main(friendIP):
    s = socket.socket()
    host = friendIP
    port = 9999
    s.connect((host, port))

    while True:
        data = s.recv(1024).decode('utf-8')

        if len(data) > 0:
            print('<<<' + str(data))

    s.close()


















