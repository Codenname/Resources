# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

# Download Pycrypto for Windows - pycrypto 2.6 for win32 py 2.7
# http://www.voidspace.org.uk/python/modules.shtml#pycrypto

# Download Pycrypto source
# https://pypi.python.org/pypi/pycrypto
# For Kali, after extract the tar file, invoke "python setup.py install"


from Crypto.PublicKey import RSA 
new_key = RSA.generate(4096 ) # generate  RSA key that 4096 bits long

#Export the Key in PEM format, the PEM extension contains ASCII encoding


public_key = new_key.publickey().exportKey("PEM") 
private_key = new_key.exportKey("PEM") 
print private_key
print public_key
