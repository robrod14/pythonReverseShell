# pythonReverseShellServer.py

Reverse Shell python script. Just open the Server file and set the IP address and the port number.

This will open the port on your attacking machine and wait for the client python script to be clicked on the victim machine.

Client file should be modified to contain the attackers IP address and port number (This information should match the Server script).  Find a way to get the victim to click on the file and you will have a reverse shell.  ***Server script must already be running***

The Data exfiltration scripts are the same asa the reverse shells except they allow for files to be transferred.  Setup is the same.  To transfer a file you must type **"grab*c:\path\to\the\file"** This will save a copy of the file on the attacking desktop as a ".PNG" file.  Just change he file extension to the real file extension and open the file as normal.

To make your python file into and exe file you must create a folder and place 3 files into the folder.  setup.py, py2exe (executable), script to convert to exe.  With these three files in the folder, make sure you have installed the correct py2exe for the OS and python you are running.  Also edit the setup.py file to contain the script you want to convert to exe and to the name of your py2exe file.

**File Description:**

Client Send_Receive_Revere_Shell.py   -    Tcp Reverse shell can send and receive files
Data Exfiltration Client - TCP Reverse Shell.py   -   TCP Reverse Shell that can ONLY get files from victims machine
Data Exfiltration Server - TCP Reverse Shell.py   -   TCP Reverse Shell that can ONLY get files from victims machine
Server Send_Reciive_Reverse_Shell.py   -    Tcp Reverse shell can send and receive files
reverseShellClient.py   -    Tcp Reverse shell can ONLY browse the exploited machine
reverseShellServer.py   -    Tcp Reverse shell can ONLY browse the exploited machine
Setup.py   -    Used when trying to change python to exe
