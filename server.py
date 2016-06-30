import socket

def socket_create():
    try:
        global host
        global port
        global s

        host = ''
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print('socket creation error:' + str(msg))

def socket_bind():
    try:
        global host
        global port
        global s

        print('binding socket to port: %s' %port)

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print('socket binding error: %s' %msg, "\n" 'Retrying...')
        socket_bind()

def socket_accept():
    conn, address = s.accept()
    print('connection has been established |' + 'IP ' + str(address[0]) + ' | Port ' + str(address[1]))
    send_messages(conn)
    print('closing connection...')
    conn.close()
    print('connection closed')
def send_messages(conn):
    while True:
        newMssg = input('>>>')

        if newMssg == 'q':
            s.close()
            break
        if len(str.encode(newMssg)) > 0:
            conn.send(str.encode(newMssg))
            continue

def main():
    socket_create()
    socket_bind()
    socket_accept()

if __name__ == "__main__":
    main()
