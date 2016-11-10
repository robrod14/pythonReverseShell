# py2exe download link: http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/
# Folder must contain python script, setup.py script, and py2exe file

from distutils.core import setup
import py2exe , sys, os



sys.argv.append("py2exe")
setup(
    options = {'py2exe-2.7': {'bundle_files': 1}},  # py2exe-2.7 must be name of your py2exe
 
    windows = [{'script': "client.py"}],    # client.py must be name of python script you want to make and exe
    zipfile = None,             # None means don't make a zipfile
    
)
