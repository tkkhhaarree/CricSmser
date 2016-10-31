# edit details.py according to your twilio credentials before running main.py.

import time, sys
from twilio.rest import TwilioRestClient
from details import sid, auth, sendto, frm
from cricbuzzcrawler import msg

if msg=="scores for the country you requested not found.":
    print(msg)
    sys.exit(2)
else:
    print ("enter time period in minutes to send SMSes: ")
    t= int(input())
    client = TwilioRestClient(sid, auth)
    while True:
         client.messages.create(to=sendto, from_=frm, body=msg)
         time.sleep(int(t*60))
