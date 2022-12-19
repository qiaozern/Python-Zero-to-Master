import os
from twilio.rest import Client

TWILIO_SID = os.environ("TWILIO_SID")
TWILIO_AUTH = os.environ("TWILIO_AUTH")
TWILIO_VISUAL_NUMBER = os.environ("TWILIO_VISUAL_NUMBER")
TWILIO_VERIFY_NUMBER = os.environ("TWILIO_VERIFY_NUMBER")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH)
    
    def send_sms(self, message):
        message = self.client.messages.create(
                     body=message,
                     from_=TWILIO_VISUAL_NUMBER,
                     to=TWILIO_VERIFY_NUMBER
                 )
        print(message.sid)