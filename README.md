# pythonReverseShellServer.py

Reverse Shell python script. Just open the Server file and set the IP address and the port number.

This will open the port on your attacking machine and wait for the client python script to be clicked on the victim machine.

Client file should be modified to contain the attackers IP address and port number (This information should match the Server script).  Find a way to get the victim to click on the file and you will have a reverse shell.  ***Server script must already be running***

The Data exfiltration scripts are the same asa the reverse shells except they allow for files to be transferred.  Setup is the same.  To transfer a file you must type **"grab*c:\path\to\the\file"** This will save a copy of the file on the attacking desktop as a ".PNG" file.  Just change he file extension to the real file extension and open the file as normal.

