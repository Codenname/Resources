'''
Caution
--------
Using this script for any malicious purpose is prohibited and against the law. Please read Twitter terms and conditions carefully. 
Use it on your own risk. 
'''


# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

#BeautifulSoup 3.2.1 download link
#https://pypi.python.org/pypi/BeautifulSoup

#Case study ? Russian Malware
#https://www2.fireeye.com/APT29-HAMMERTOSS-WEB-2015-RPT.html
#https://www.fireeye.com/blog/threat-research/2015/07/hammertoss_stealthy.html



from BeautifulSoup import BeautifulSoup as soupy
import urllib
import re


html = urllib.urlopen('https://twitter.com/tferriss').read()
soup = soupy(html)
#Navigate to my twitter home page HussamKhrais, store the HTML page into html variable and pass it
#to soupy function so we can parse it


x = soup.find("meta", {"name":"description"})['content']
#Here we search for specific HTML meta tags, please see the video to know how did i find these parameters :) 


filter = re.findall(r'"(.*?)"',x)  # After parsing the html page, our tweet is located between double quotations
tweet =  filter[0]                 # using regular expression we filter out the tweet  
print tweet



