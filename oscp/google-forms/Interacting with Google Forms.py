'''
Caution
--------
Using this script for any malicious purpose is prohibited and against the law. Please read Google terms and conditions carefully. 
Use it on your own risk. 
'''

# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2



import requests   # To install requests library, just type on the CMD:  pip install requests

url = 'https://docs.google.com/forms/YOURLINK/formResponse' # please replace the URL with your own google form :D

'''
notice that i added  /formResponse  to the end of the URL and this is inherited from the  page HTML source code,
as we can see below, the HTML form action contains /formResponse when method POST is used to send the user data
so we have to add this part when we automate the data submission


<div class="ss-form"><form action="https://docs.google.com/forms/d/1Ndjnm5YViqIYXyIuoTHsCqW_YfGa-vaaKEahY2cc5cs/formResponse?pli=1"
method="POST" id="ss-form" target="_self" onsubmit=""><ol role="list" class="ss-question-list" style="padding-left: 0">
'''


form_data = {'entry.123number':"ENTRY"}

'''
the textarea form name [which is entry.1301128713] can be taken from the HTML source code as you can see from the below line,
please check the video for more info.

<textarea name="entry.1301128713" rows="8" cols="0" class="ss-q-long" id="entry_1301128713" dir="auto" aria-label="Isn&#39;t Python awesome??  "></textarea>

Note: the key (entry.1301128713) will vary on your google form, make sure you change it. 
'''


r = requests.post(url, data=form_data)
# Submitting form-encoded data in requests:-
# http://docs.python-requests.org/en/latest/user/quickstart/#more-complicated-post-requests



